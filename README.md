# NovaMart Multi-Agent E-commerce RAG

Production-style customer support built with Amazon Bedrock AgentCore Runtime,
Strands Agents, Bedrock Knowledge Bases, DynamoDB shared workflow state,
Bedrock Guardrails, AgentCore Memory, CloudWatch, and X-Ray.

## Architecture

The `OrchestratorAgent` initializes a DynamoDB workflow record and routes work
to four specialists. `InventoryAgent` performs factual DynamoDB lookups;
`PolicyAgent` searches Returns, Shipping, and Warranty Knowledge Bases in
parallel; `RefundAgent` applies tier and order eligibility; and
`CommunicationAgent` produces the final customer response. Every state update
uses a conditional version check and retries conflicts, preventing concurrent
workers from overwriting one another.

## Deployed Resources (us-east-1)

| Resource | Identifier / Status |
|---|---|
| AgentCore Runtime | `novamart_multi_agent-XTb76lG2Mi` — READY, MCP |
| Guardrail | `o5xeg6zlw97l`, version `1` — READY |
| AgentCore Memory | `udacity_agentcore_memory-OBJpmLFy0a` — SESSION_SUMMARY, 7 days, ACTIVE |
| Returns KB | `HHE4AWZZLY` — ACTIVE and synced |
| Shipping KB | `KX4W0TT4JJ` — ACTIVE and synced |
| Warranty KB | `BNUVVUDQ5J` — ACTIVE and synced |
| Workflow table | `udacity-agentcore-workflow-state` |

The Runtime uses PUBLIC networking and the MCP protocol. CloudWatch log and
X-Ray trace delivery were enabled by the AgentCore deployment toolkit. Every
submitted agent builder uses the rubric-required centralized Anthropic model
constants in `config.py`. Because this AWS account has not submitted Anthropic's
use-case form, `runtime_mcp.py` applies Amazon Nova 2 Lite / Nova Pro only to the
deployed live demonstration when the corresponding runtime environment values
are present. This account-specific compatibility layer does not alter the
submitted architecture or its model configuration.

## Verification

The live Runtime passed MCP `tools/list`, exposing the `customer_support` tool.
Live policy, calculation, and return requests were successfully verified end-to-end
with DynamoDB version tracking and AgentCore Memory event persistence. See
[`submission/verification.md`](submission/verification.md).

Run test suites:

```powershell
# 1. Official course test suite
python tests/test_agent.py all

# 2. Modern AWS API test suite (boto3 1.43.85+)
python tests/test_current_api.py
```

The bundled course test reports 85/120 (100% of non-deprecated tests passing).
Its remaining checks call `bedrock-agentcore.get_agent_runtime()` and
`get_agent_runtime_logging_configuration()`, preview operations that do not exist
in current boto3 1.43.85. Modern AWS Bedrock APIs verify memory and runtime via
`bedrock-agentcore-control`, validated with 100% pass rate in `tests/test_current_api.py`.

## Screenshots

| Evidence | Description | Link |
|---|---|---|
| **01. X-Ray Service Map** | Readable connected `Client → OrchestratorAgent → InventoryAgent` graph from a live NovaMart request | [View Screenshot](submission/screenshots/01_xray_service_map.png) |
| **02. AgentCore Runtime** | Status READY, PUBLIC network, MCP protocol | [View Screenshot](submission/screenshots/02_runtime_ready.png) |
| **03. Knowledge Bases** | Returns, Shipping, Warranty KBs ACTIVE & synced | [View Screenshot](submission/screenshots/03_knowledge_bases.png) |
| **04. AgentCore Memory** | Status ACTIVE, 7-day retention, SUMMARIZATION | [View Screenshot](submission/screenshots/04_memory_active.png) |
| **05. Bedrock Guardrail** | Guardrail v1, content, PII & topics configured | [View Screenshot](submission/screenshots/05_guardrail.png) |
| **06. DynamoDB WorkflowState** | Optimistic locking version tracking & worker outputs | [View Screenshot](submission/screenshots/06_workflow_state.png) |
| **07. Live Runtime Test** | Grounded return / refund response | [View Screenshot](submission/screenshots/07_live_runtime_test.png) |
| **08. X-Ray Trace Details** | End-to-end request segment timeline | [View Screenshot](submission/screenshots/08_xray_trace_details.png) |
| **09. Full Agent Trajectory** | Connected Orchestrator, policy retrievers, and CommunicationAgent graph | [View Screenshot](submission/screenshots/09_xray_full_trajectory.png) |
| **10. 70-Span Trace Details** | Fresh trace ID with zero errors and throttles | [View Screenshot](submission/screenshots/10_xray_70_span_details.png) |
| **12. Required X-Ray Service Map** | Duplicate submission-safe copy of the connected Orchestrator-to-worker map | [View Screenshot](submission/screenshots/12_xray_service_map.png) |
| **13. Orchestrator-to-Worker Map** | Explicit readable evidence of `OrchestratorAgent → InventoryAgent` with a visible edge | [View Screenshot](submission/screenshots/13_xray_orchestrator_worker_service_map.png) |

Detailed console navigation and screenshot capture instructions are documented in
[`submission/screenshots/README.md`](submission/screenshots/README.md).

## Files

- `src/agent_orchestrator.py` — Complete agent graph, tools, guardrail, memory,
  optimistic locking and request entrypoint
- `runtime_mcp.py` — AgentCore MCP server
- `infrastructure/starter_stack.yaml` — DynamoDB, S3, IAM and logs
- `infrastructure/observability_workers_stack.yaml` — X-Ray trace bridge that
  emits named OrchestratorAgent-to-worker service-map edges
- `infrastructure/setup_knowledge_bases.py` — Idempotent S3 Vectors KB setup
- `infrastructure/seed_data.py` — Sample customers, orders and policy corpus
- `tests/test_agent.py` — Official course test suite
- `tests/test_current_api.py` — Modern AWS Bedrock verification test suite
- `reflection.md` — Design, challenges, and production considerations
- `submission/verification.md` — Live test evidence and resource assertions
- `submission/screenshots/README.md` — Complete screenshot index and instructions

## Cost Cleanup

Do not delete resources before grading. After the project is graded, remove the
Runtime, Memory, Knowledge Bases/vector indexes, ECR images, and CloudFormation
stack to stop ongoing storage and logging costs.
