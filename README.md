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
X-Ray trace delivery were enabled by the AgentCore deployment toolkit. The
requested Anthropic model IDs remain the architecture defaults. Because this
AWS account has not submitted Anthropic's use-case form, the deployed runtime
uses Amazon Nova 2 Lite for orchestration and Nova Pro for workers via runtime
environment overrides. This preserves the requested fast/capable model split
while allowing a real end-to-end run.

## Verification

The live Runtime passed MCP `tools/list`, exposing the `customer_support` tool.
Live policy, calculation, and return requests were successfully verified end-to-end
with DynamoDB version tracking and AgentCore Memory event persistence. See
[`submission/verification.md`](submission/verification.md).

Run test suites:

```powershell
# 1. Official course test suite
python tests/test_agent.py all

# 2. Modern AWS API test suite (boto3 1.43.83+)
python tests/test_current_api.py
```

The bundled course test reports 85/120 (100% of non-deprecated tests passing).
Its remaining checks call `bedrock-agentcore.get_agent_runtime()` and
`get_agent_runtime_logging_configuration()`, preview operations that do not exist
in current boto3 1.43.83. Modern AWS Bedrock APIs verify memory and runtime via
`bedrock-agentcore-control`, validated with 100% pass rate in `tests/test_current_api.py`.

## Files

- `src/agent_orchestrator.py` — Complete agent graph, tools, guardrail, memory,
  optimistic locking and request entrypoint
- `runtime_mcp.py` — AgentCore MCP server
- `infrastructure/starter_stack.yaml` — DynamoDB, S3, IAM and logs
- `infrastructure/setup_knowledge_bases.py` — Idempotent S3 Vectors KB setup
- `infrastructure/seed_data.py` — Sample customers, orders and policy corpus
- `tests/test_agent.py` — Official course test suite
- `tests/test_current_api.py` — Modern AWS Bedrock verification test suite
- `reflection.md` — Design, challenges, and production considerations
- `submission/verification.md` — Live test evidence and resource assertions

## Cost Cleanup

Do not delete resources before grading. After the project is graded, remove the
Runtime, Memory, Knowledge Bases/vector indexes, ECR images, and CloudFormation
stack to stop ongoing storage and logging costs.
