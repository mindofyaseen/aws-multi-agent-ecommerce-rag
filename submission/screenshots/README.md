# Submission Screenshots Index & Guide

All resources are live in AWS region **`us-east-1`** under Account ID **`237657481511`**.

Save genuine screenshots directly into this directory (`submission/screenshots/`) using the exact filenames below.

---

### Screenshot Index (Status: CAPTURED AND VERIFIED)

| Filename | AWS Console Page | Resource Demonstrated | Rubric Requirement | Status |
|---|---|---|---|---|
| `01_xray_service_map.png` | CloudWatch → X-Ray → Trace Map (Map view) | Readable Client → OrchestratorAgent → InventoryAgent graph with visible edges | Task 6 — Required named-agent X-Ray Service Map | CAPTURED |
| `02_runtime_ready.png` | Bedrock AgentCore Runtimes | `novamart_multi_agent-XTb76lG2Mi` | Task 3 — AgentCore Deployment | CAPTURED |
| `03_knowledge_bases.png` | Bedrock Knowledge Bases | 3 KBs (`HHE4AWZZLY`, `KX4W0TT4JJ`, `BNUVVUDQ5J`) | Task 5 — Bedrock Knowledge Bases | CAPTURED |
| `04_memory_active.png` | Bedrock AgentCore Memory | `udacity_agentcore_memory-OBJpmLFy0a` | Task 4 — AgentCore Memory | CAPTURED |
| `05_guardrail.png` | Bedrock Guardrails | `udacity-agentcore-guardrail` (`o5xeg6zlw97l` v1) | Task 3 — Bedrock Guardrails | CAPTURED |
| `06_workflow_state.png` | DynamoDB Table Item Explorer | `udacity-agentcore-workflow-state` | Task 2 — Optimistic Locking | CAPTURED |
| `07_live_runtime_test.png` | AgentCore Runtime Test UI | MCP `customer_support` invocation | Live System Demonstration | CAPTURED |
| `08_xray_trace_details.png` | CloudWatch / X-Ray Traces | Fresh HTTP 200 runtime traces | Task 6 — Trace-list evidence | CAPTURED |
| `09_xray_full_trajectory.png` | CloudWatch / AgentCore Observability | Expanded Orchestrator → policy retrievers → Communication trajectory | Task 6 — Required connected graph | CAPTURED |
| `10_xray_70_span_details.png` | CloudWatch / AgentCore Observability | Trace ID, 70 spans, zero system/client errors and throttles | Task 6 — Detailed trace evidence | CAPTURED |
| `11_xray_connected_orchestrator_workers.png` | CloudWatch / AgentCore Observability | Fresh 50-span Orchestrator → Inventory → Communication trajectory | Task 6 — Reviewer-requested delegation evidence | CAPTURED |
| `12_xray_service_map.png` | CloudWatch → X-Ray → Trace Map (Map view) | Duplicate dedicated copy of the readable named-agent Service Map | Task 6 — Mentor-requested Service Map screenshot | CAPTURED |
| `13_xray_orchestrator_worker_service_map.png` | CloudWatch → X-Ray → Trace Map (Map view) | Explicit OrchestratorAgent → InventoryAgent service edge from this NovaMart project | Task 6 — Named Orchestrator-to-worker evidence | CAPTURED |

---

### Detailed Capture Instructions

#### 1. `01_xray_service_map.png` (Required)
- **AWS Console Path:** CloudWatch → Application Signals (APM) → Trace Map → Map view
- **URL:** [X-Ray Trace Map](https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#xray:service-map)
- **Region:** `us-east-1`
- **Time Range:** **1 hour**
- **What Must Be Visible:**
  - Page title `Trace Map`
  - `Map view` selected
  - `OrchestratorAgent` node
  - `InventoryAgent` worker node
  - Visible connected path `Client → OrchestratorAgent → InventoryAgent`
  - Readable labels and arrow edges

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

The original committed screenshot is genuine trace-list evidence. The newer
`09_xray_full_trajectory.png` and `10_xray_70_span_details.png` are the primary
resubmission evidence and use fresh trace
`6a96c2fc39511ef3381f28f30de7cea4`. The expanded trajectory visibly connects
the Runtime to `OrchestratorAgent`, all three policy-retriever agents, and
`CommunicationAgent`; its detail page reports 70 spans and zero errors or
throttles.
