"""Idempotently create and sync NovaMart's three S3 Vectors Knowledge Bases."""
import json
import os
import sys
import time
from pathlib import Path

import boto3

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config

agent = boto3.client("bedrock-agent", region_name=config.AWS_REGION)
vectors = boto3.client("s3vectors", region_name=config.AWS_REGION)


def wait_kb(kb_id):
    for _ in range(80):
        status = agent.get_knowledge_base(knowledgeBaseId=kb_id)["knowledgeBase"]["status"]
        if status == "ACTIVE":
            return
        if status in {"FAILED", "DELETE_UNSUCCESSFUL"}:
            raise RuntimeError(f"Knowledge Base {kb_id} entered {status}")
        time.sleep(5)
    raise TimeoutError(f"Knowledge Base {kb_id} did not become ACTIVE")


def existing_kbs():
    result = {}
    for page in agent.get_paginator("list_knowledge_bases").paginate():
        for kb in page.get("knowledgeBaseSummaries", []):
            result[kb["name"]] = kb["knowledgeBaseId"]
    return result


def main():
    vector_name = f"{config.PROJECT_NAME}-vectors-{config.ACCOUNT_ID}"
    try:
        bucket = vectors.get_vector_bucket(vectorBucketName=vector_name)
    except vectors.exceptions.NotFoundException:
        bucket = vectors.create_vector_bucket(vectorBucketName=vector_name)
    vector_arn = bucket["vectorBucket"]["vectorBucketArn"] if "vectorBucket" in bucket else bucket["vectorBucketArn"]
    found = existing_kbs()
    ids = {}
    model_arn = f"arn:aws:bedrock:{config.AWS_REGION}::foundation-model/amazon.titan-embed-text-v2:0"
    for domain in ("returns", "shipping", "warranty"):
        name = f"novamart-{domain}-policy-kb"
        index_name = f"novamart-{domain}-index"
        try:
            index = vectors.get_index(vectorBucketName=vector_name, indexName=index_name)
        except vectors.exceptions.NotFoundException:
            index = vectors.create_index(
                vectorBucketName=vector_name, indexName=index_name,
                dataType="float32", dimension=1024, distanceMetric="cosine",
                metadataConfiguration={"nonFilterableMetadataKeys": ["AMAZON_BEDROCK_TEXT", "AMAZON_BEDROCK_METADATA"]},
            )
        index_arn = index["index"]["indexArn"] if "index" in index else index["indexArn"]
        kb_id = found.get(name)
        if not kb_id:
            response = agent.create_knowledge_base(
                name=name, description=f"NovaMart {domain} policies",
                roleArn=config.AGENTCORE_ROLE_ARN,
                knowledgeBaseConfiguration={
                    "type": "VECTOR",
                    "vectorKnowledgeBaseConfiguration": {"embeddingModelArn": model_arn,
                        "embeddingModelConfiguration": {"bedrockEmbeddingModelConfiguration": {"dimensions": 1024, "embeddingDataType": "FLOAT32"}}},
                },
                storageConfiguration={"type": "S3_VECTORS", "s3VectorsConfiguration": {
                    "vectorBucketArn": vector_arn, "indexArn": index_arn,
                }},
            )
            kb_id = response["knowledgeBase"]["knowledgeBaseId"]
        wait_kb(kb_id)
        data_sources = agent.list_data_sources(knowledgeBaseId=kb_id).get("dataSourceSummaries", [])
        if data_sources:
            ds_id = data_sources[0]["dataSourceId"]
        else:
            ds = agent.create_data_source(
                knowledgeBaseId=kb_id, name=f"novamart-{domain}-s3-source",
                dataSourceConfiguration={"type": "S3", "s3Configuration": {
                    "bucketArn": f"arn:aws:s3:::{config.POLICY_BUCKET}",
                    "inclusionPrefixes": [f"policies/{domain}/"],
                }},
                vectorIngestionConfiguration={"chunkingConfiguration": {
                    "chunkingStrategy": "FIXED_SIZE", "fixedSizeChunkingConfiguration": {
                        "maxTokens": 300, "overlapPercentage": 20,
                    }}},
            )
            ds_id = ds["dataSource"]["dataSourceId"]
        job = agent.start_ingestion_job(knowledgeBaseId=kb_id, dataSourceId=ds_id)["ingestionJob"]
        for _ in range(80):
            current = agent.get_ingestion_job(knowledgeBaseId=kb_id, dataSourceId=ds_id,
                                              ingestionJobId=job["ingestionJobId"])["ingestionJob"]
            if current["status"] == "COMPLETE":
                break
            if current["status"] == "FAILED":
                raise RuntimeError(current.get("failureReasons"))
            time.sleep(5)
        ids[domain] = kb_id
        print(f"{domain}: {kb_id} synced")
    print(json.dumps(ids))


if __name__ == "__main__":
    main()
