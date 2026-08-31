"""
test_current_api.py
===================
Modern AWS API verification test suite for the NovaMart Multi-Agent System.

Validates all 6 tasks against current (boto3 1.43.83+) AWS Bedrock APIs:
  - Task 2: Multi-Agent Orchestration & tools
  - Task 3: AgentCore Runtime & Bedrock Guardrail
  - Task 4: AgentCore SESSION_SUMMARY Memory
  - Task 5: Three active Bedrock Knowledge Bases (Returns, Shipping, Warranty)
  - Task 6: Observability (CloudWatch Log Group & live X-Ray traces)
"""

import os
import sys
import unittest
import boto3
import datetime
from pathlib import Path

# Add project root and src to path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
sys.path.insert(0, str(ROOT))

import config
import agent_orchestrator as ao


class TestTask2Orchestration(unittest.TestCase):
    def test_inventory_agent_tools(self):
        agent = ao.build_inventory_agent()
        self.assertIsNotNone(agent)
        reg = getattr(agent, 'tool_registry', None)
        tools = getattr(reg, 'registry', {}) if reg else {}
        self.assertEqual(len(tools), 3, "InventoryAgent must have exactly 3 tools")
        self.assertIn("check_order_status", tools)
        self.assertIn("get_customer_tier", tools)
        self.assertIn("list_customer_orders", tools)

    def test_policy_agent_tools(self):
        agent = ao.build_policy_agent()
        self.assertIsNotNone(agent)
        reg = getattr(agent, 'tool_registry', None)
        tools = getattr(reg, 'registry', {}) if reg else {}
        self.assertEqual(len(tools), 1, "PolicyAgent must have exactly 1 tool")
        self.assertIn("search_all_policies", tools)

    def test_orchestrator_agent_tools(self):
        inv = ao.build_inventory_agent()
        ref = ao.build_refund_agent()
        pol = ao.build_policy_agent()
        com = ao.build_communication_agent()
        orch = ao.build_orchestrator_agent(inv, ref, pol, com)
        self.assertIsNotNone(orch)
        reg = getattr(orch, 'tool_registry', None)
        tools = getattr(reg, 'registry', {}) if reg else {}
        self.assertEqual(len(tools), 5, "OrchestratorAgent must have exactly 5 routing tools")

    def test_model_architecture_defaults(self):
        self.assertIn("haiku", config.ORCHESTRATOR_MODEL_ID.lower())
        self.assertIn("sonnet", config.WORKER_MODEL_ID.lower())


class TestTask3RuntimeAndGuardrail(unittest.TestCase):
    def setUp(self):
        self.bedrock = boto3.client('bedrock', region_name=config.AWS_REGION)
        self.agentcore_ctrl = boto3.client('bedrock-agentcore-control', region_name=config.AWS_REGION)

    def test_guardrail_configuration(self):
        guardrail_id = config.GUARDRAIL_ID
        self.assertTrue(bool(guardrail_id), "GUARDRAIL_ID must be set")
        res = self.bedrock.get_guardrail(
            guardrailIdentifier=guardrail_id,
            guardrailVersion=config.GUARDRAIL_VERSION
        )
        self.assertEqual(res.get('status'), 'READY')
        self.assertIn('contentPolicy', res)
        self.assertIn('sensitiveInformationPolicy', res)
        self.assertIn('topicPolicy', res)
        self.assertIn('wordPolicy', res)

    def test_runtime_status(self):
        runtime_arn = config.AGENTCORE_RUNTIME_ARN
        self.assertTrue(bool(runtime_arn), "AGENTCORE_RUNTIME_ARN must be set")
        runtime_id = runtime_arn.split('/')[-1]
        res = self.agentcore_ctrl.get_agent_runtime(agentRuntimeId=runtime_id)
        self.assertEqual(res.get('status'), 'READY')
        self.assertEqual(res.get('protocolConfiguration', {}).get('serverProtocol'), 'MCP')
        self.assertEqual(res.get('networkConfiguration', {}).get('networkMode'), 'PUBLIC')


class TestTask4AgentCoreMemory(unittest.TestCase):
    def setUp(self):
        self.agentcore_ctrl = boto3.client('bedrock-agentcore-control', region_name=config.AWS_REGION)

    def test_memory_active_and_configured(self):
        mem_id = os.environ.get('MEMORY_ID', 'udacity_agentcore_memory-OBJpmLFy0a')
        res = self.agentcore_ctrl.get_memory(memoryId=mem_id)
        memory = res.get('memory', {})
        self.assertEqual(memory.get('status'), 'ACTIVE')
        self.assertEqual(memory.get('eventExpiryDuration'), 7)
        strategies = memory.get('strategies', [])
        self.assertTrue(any(s.get('type') == 'SUMMARIZATION' for s in strategies))


class TestTask5KnowledgeBases(unittest.TestCase):
    def setUp(self):
        self.bedrock_agent = boto3.client('bedrock-agent', region_name=config.AWS_REGION)

    def test_three_kbs_active(self):
        for kb_id in [config.RETURNS_KB_ID, config.SHIPPING_KB_ID, config.WARRANTY_KB_ID]:
            self.assertTrue(bool(kb_id), f"KB ID {kb_id} must be set")
            res = self.bedrock_agent.get_knowledge_base(knowledgeBaseId=kb_id)
            self.assertEqual(res.get('knowledgeBase', {}).get('status'), 'ACTIVE')


class TestTask6Observability(unittest.TestCase):
    def setUp(self):
        self.logs = boto3.client('logs', region_name=config.AWS_REGION)
        self.xray = boto3.client('xray', region_name=config.AWS_REGION)

    def test_cloudwatch_and_xray(self):
        log_res = self.logs.describe_log_groups(logGroupNamePrefix=config.AGENT_LOG_GROUP)
        self.assertTrue(len(log_res.get('logGroups', [])) > 0, "CloudWatch log group must exist")
        
        now = datetime.datetime.now(datetime.timezone.utc)
        xray_res = self.xray.get_trace_summaries(
            StartTime=now - datetime.timedelta(hours=4),
            EndTime=now
        )
        self.assertTrue(len(xray_res.get('TraceSummaries', [])) > 0, "X-Ray traces must be recorded")


if __name__ == '__main__':
    unittest.main(verbosity=2)
