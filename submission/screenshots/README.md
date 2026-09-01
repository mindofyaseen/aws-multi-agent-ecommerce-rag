# Submission Screenshots Index & Guide

All resources are live in AWS region **`us-east-1`** under Account ID **`237657481511`**.

Save genuine screenshots directly into this directory (`submission/screenshots/`) using the exact filenames below.

---

### Screenshot Index (Status: CAPTURED AND VERIFIED)

| Filename | AWS Console Page | Resource Demonstrated | Rubric Requirement | Status |
|---|---|---|---|---|
| `01_xray_service_map.png` | CloudWatch / X-Ray Service Map | `novamart_multi_agent.DEFAULT` | Task 6 — Observability & Tracing | CAPTURED |
| `02_runtime_ready.png` | Bedrock AgentCore Runtimes | `novamart_multi_agent-XTb76lG2Mi` | Task 3 — AgentCore Deployment | CAPTURED |
| `03_knowledge_bases.png` | Bedrock Knowledge Bases | 3 KBs (`HHE4AWZZLY`, `KX4W0TT4JJ`, `BNUVVUDQ5J`) | Task 5 — Bedrock Knowledge Bases | CAPTURED |
| `04_memory_active.png` | Bedrock AgentCore Memory | `udacity_agentcore_memory-OBJpmLFy0a` | Task 4 — AgentCore Memory | CAPTURED |
| `05_guardrail.png` | Bedrock Guardrails | `udacity-agentcore-guardrail` (`o5xeg6zlw97l` v1) | Task 3 — Bedrock Guardrails | CAPTURED |
| `06_workflow_state.png` | DynamoDB Table Item Explorer | `udacity-agentcore-workflow-state` | Task 2 — Optimistic Locking | CAPTURED |
| `07_live_runtime_test.png` | AgentCore Runtime Test UI | MCP `customer_support` invocation | Live System Demonstration | CAPTURED |
| `08_xray_trace_details.png` | CloudWatch / X-Ray Traces | Fresh HTTP 200 runtime traces | Task 6 — Trace-list evidence | CAPTURED |

---

### Detailed Capture Instructions

#### 1. `01_xray_service_map.png` (Required)
- **AWS Console Path:** CloudWatch → X-Ray traces → Service map  
- **URL:** [X-Ray Service Map](https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#xray:service-map) or [GenAI Observability](https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#gen-ai-observability/agent-core)
- **Region:** `us-east-1`
- **Time Range:** Select **1 hour** or **3 hours** (containing recent live requests)
- **What Must Be Visible:**
  - Service node `novamart_multi_agent.DEFAULT`
  - Connected client / service edges with 100% 200 OK responses
  - Service latency & throughput stats

#### 2. `02_runtime_ready.png`
- **AWS Console Path:** Amazon Bedrock → AgentCore → Runtimes → `novamart_multi_agent`
- **URL:** [Bedrock AgentCore Runtimes](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/agentcore)
- **Region:** `us-east-1`
- **What Must Be Visible:**
  - Runtime Name: `novamart_multi_agent`
  - Runtime ID: `novamart_multi_agent-XTb76lG2Mi`
  - Status: `READY`
  - Protocol: `MCP`
  - Network Configuration: `PUBLIC`

#### 3. `03_knowledge_bases.png` (or `03a_returns_kb.png`, `03b_shipping_kb.png`, `03c_warranty_kb.png`)
- **AWS Console Path:** Amazon Bedrock → Builder tools → Knowledge bases
- **URL:** [Bedrock Knowledge Bases](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/knowledge-bases)
- **Region:** `us-east-1`
- **What Must Be Visible:**
  - `novamart-returns-policy-kb` (`HHE4AWZZLY`) — Status: `Ready` / `Active`
  - `novamart-shipping-policy-kb` (`KX4W0TT4JJ`) — Status: `Ready` / `Active`
  - `novamart-warranty-policy-kb` (`BNUVVUDQ5J`) — Status: `Ready` / `Active`
  - Data sources showing synced status

#### 4. `04_memory_active.png`
- **AWS Console Path:** Amazon Bedrock → AgentCore → Memory → `udacity_agentcore_memory`
- **URL:** [Bedrock AgentCore Memory](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/agentcore)
- **Region:** `us-east-1`
- **What Must Be Visible:**
  - Memory ID: `udacity_agentcore_memory-OBJpmLFy0a`
  - Status: `ACTIVE`
  - Strategy: `SUMMARIZATION` (`udacity_agentcore_memory_summary`)
  - Event expiry: 7 days

#### 5. `05_guardrail.png` (or `05a_overview.png`, `05b_content.png`, `05c_pii_topics.png`)
- **AWS Console Path:** Amazon Bedrock → Safeguards → Guardrails → `udacity-agentcore-guardrail`
- **URL:** [Bedrock Guardrails](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/guardrails)
- **Region:** `us-east-1`
- **What Must Be Visible:**
  - Guardrail Name: `udacity-agentcore-guardrail`
  - ID: `o5xeg6zlw97l` | Version: `1`
  - Status: `READY`
  - Content filters: HIGH (Sexual, Violence, Hate), MEDIUM (Insults, Misconduct)
  - Sensitive info filters: PII (Credit card, SSN blocked; Email, Phone anonymized)
  - Denied topics: `competitor products`, `pricing negotiations`, `legal threats`
  - Managed profanity list enabled

#### 6. `06_workflow_state.png`
- **AWS Console Path:** DynamoDB → Tables → `udacity-agentcore-workflow-state` → Explore table items
- **URL:** [DynamoDB Table Items](https://us-east-1.console.aws.amazon.com/dynamodbv2/home?region=us-east-1#item-explorer?table=udacity-agentcore-workflow-state)
- **Region:** `us-east-1`
- **What Must Be Visible:**
  - Items in table with `session_id` (e.g. `session-8babf52ec4a643278c2079d4200c6071`)
  - `version` showing integer increment (e.g. 3)
  - Populated attributes: `customer_id`, `inventory_agent`, `refund_agent`, `communication_agent`

#### 7. `07_live_runtime_test.png`
- **Interface:** Terminal or Bedrock AgentCore Runtime Test console
- **What Must Be Visible:**
  - Live customer return request (e.g. `"I want to return my order ORD-35244."`)
  - Grounded refund approval response with return reference `RET-F25168A465`
  - `isError: false` and HTTP 200 status

#### 8. `08_xray_trace_details.png`
- **AWS Console Path:** CloudWatch → X-Ray traces → Traces → Click on a trace ID
- **URL:** [X-Ray Traces](https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#xray:traces)
- **Region:** `us-east-1`
- **Verified full-chain trace ID:** `6a95b4211d7df5dd07e3e8687b916946`
- **What Must Be Visible:**
  - Trace ID header
  - Span count (`70`) and successful status
  - `OrchestratorAgent`, `PolicyAgent`, all three named policy retrievers,
    `CommunicationAgent`, and their associated tool spans
  - Total duration and zero system/client errors

The committed screenshot is genuine trace-list evidence. Before resubmission, a
single expanded trace-detail capture of the verified trace above is preferred
because it makes the complete worker chain visible to the reviewer at a glance.
