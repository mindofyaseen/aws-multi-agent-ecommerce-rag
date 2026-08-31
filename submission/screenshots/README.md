# Submission Screenshots Guide

All resources are live in `us-east-1` under Account ID `237657481511`.

Capture and save genuine screenshots to this folder using the filenames below:

---

### 1. `01_xray_service_map.png` (Required)
- **AWS Console Page:** CloudWatch / X-Ray GenAI Observability or Service Map
- **URL:** [CloudWatch GenAI Observability](https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#gen-ai-observability/agent-core) or [X-Ray Service Map](https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#xray:service-map)
- **Region:** `us-east-1`
- **Resource:** Service `novamart_multi_agent.DEFAULT`
- **What Must Be Visible:**
  - Region `us-east-1` in header
  - Service node `novamart_multi_agent.DEFAULT`
  - Successful 200 responses, latency, and trace list (e.g., `1-6a957407-448fd6b623e66f7faa6d7658`)

---

### 2. `02_runtime_ready.png`
- **AWS Console Page:** Amazon Bedrock AgentCore Runtimes
- **URL:** [Bedrock AgentCore Runtimes](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/agentcore)
- **Region:** `us-east-1`
- **Resource:** `novamart_multi_agent-XTb76lG2Mi`
- **What Must Be Visible:**
  - Status: `READY`
  - Network: `PUBLIC`
  - Protocol: `MCP`
  - Runtime ARN / ID

---

### 3. `03_knowledge_bases.png`
- **AWS Console Page:** Amazon Bedrock Knowledge Bases
- **URL:** [Bedrock Knowledge Bases](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/knowledge-bases)
- **Region:** `us-east-1`
- **Resources:**
  - `novamart-returns-policy-kb` (`HHE4AWZZLY`)
  - `novamart-shipping-policy-kb` (`KX4W0TT4JJ`)
  - `novamart-warranty-policy-kb` (`BNUVVUDQ5J`)
- **What Must Be Visible:**
  - All 3 Knowledge Bases showing status `Ready` / `Active`
  - Data sources synced

---

### 4. `04_memory_active.png`
- **AWS Console Page:** Amazon Bedrock AgentCore Memory
- **URL:** [Bedrock AgentCore](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/agentcore)
- **Region:** `us-east-1`
- **Resource:** `udacity_agentcore_memory-OBJpmLFy0a`
- **What Must Be Visible:**
  - Memory ID / Name: `udacity_agentcore_memory-OBJpmLFy0a`
  - Status: `ACTIVE`
  - Strategy: `SUMMARIZATION` (`udacity_agentcore_memory_summary`)
  - Retention: 7 days

---

### 5. `05_guardrail.png`
- **AWS Console Page:** Amazon Bedrock Guardrails
- **URL:** [Bedrock Guardrails](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/guardrails)
- **Region:** `us-east-1`
- **Resource:** `udacity-agentcore-guardrail` (`o5xeg6zlw97l`) Version `1`
- **What Must Be Visible:**
  - Guardrail version `1` (READY)
  - Content filter strengths (HIGH / MEDIUM)
  - Sensitive information PII policies (BLOCK / ANONYMIZE)
  - Denied topics (`competitor products`, `pricing negotiations`, `legal threats`)
  - Managed profanity list enabled

---

### 6. `06_workflow_state.png`
- **AWS Console Page:** DynamoDB Item Explorer
- **URL:** [DynamoDB Table Item Explorer](https://us-east-1.console.aws.amazon.com/dynamodbv2/home?region=us-east-1#item-explorer?table=udacity-agentcore-workflow-state)
- **Region:** `us-east-1`
- **Resource:** Table `udacity-agentcore-workflow-state`
- **What Must Be Visible:**
  - Item with `session_id`
  - `version` (e.g. 3)
  - `inventory_agent`, `refund_agent`, `communication_agent` populated attributes
