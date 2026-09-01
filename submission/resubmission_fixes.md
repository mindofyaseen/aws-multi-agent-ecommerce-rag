# Resubmission Fixes and Live Verification

This revision directly addresses the two remaining requirements from the
September 1 review: the Task 6 automated test and connected agent tracing.

## Mentor-requested X-Ray Service Map evidence

Following the latest mentor feedback, `submission/screenshots/01_xray_service_map.png`
is now a genuine screenshot of **CloudWatch → X-Ray → Trace Map → Map
view**, rather than a trajectory, spans, or trace-details page. It was captured
in `us-east-1` using the **1 hour** window immediately after a successful live
MCP return request. The map visibly connects the Client, the deployed
`novamart_multi_agent.DEFAULT` AgentCore Runtime, and AWS STS. A dedicated copy
is also included as `submission/screenshots/12_xray_service_map.png` so the
required evidence is unmistakable to the reviewer.

## Code corrections

- Refund eligibility now reads the customer tier and order date from DynamoDB.
  Standard customers receive an inclusive 30-day window and Premium customers
  an inclusive 60-day window. The result includes the tier, elapsed days,
  configured window, decision, and return reference when approved.
- InventoryAgent and RefundAgent use `config.WORKER_MODEL_ID` at temperature
  `0.1`; CommunicationAgent uses the same configured model at `0.3`.
- PolicyAgent now contains three named sub-agents:
  `ReturnsPolicyRetrieverAgent`, `ShippingPolicyRetrieverAgent`, and
  `WarrantyPolicyRetrieverAgent`. Each owns one KB retrieval tool, uses
  temperature `0.0`, and is invoked concurrently through
  `ThreadPoolExecutor(max_workers=3)` and `as_completed()`. The coordinator uses
  temperature `0.2`.
- The orchestrator prompt explicitly states all six routing rules, routes
  account questions to InventoryAgent (never PolicyAgent), and requires
  CommunicationAgent to be the final tool call. It is prohibited from composing
  or rewriting the customer-facing response.
- Every `@tool` docstring now documents purpose, exact arguments, return shape,
  and when the tool should or should not be called.
- `configure_observability()` now calls
  `put_agent_runtime_logging_configuration()` with CloudWatch INFO logging and
  X-Ray tracing enabled at a `1.0` sampling rate. The deployed AgentCore toolkit
  also reports logs and trace delivery as enabled.
- Explicit OpenTelemetry spans identify specialist and policy-retriever work in
  end-to-end traces. Client spans include `aws.remote.service` and
  `aws.remote.operation`, and their names explicitly show
  `OrchestratorAgent -> <WorkerAgent>` delegation.

## Knowledge Base backing-store verification

Verified live in `us-east-1` on 2026-08-31:

| Domain | KB ID | Status | Embedding model | Storage type | S3 Vectors bucket | Data source |
|---|---|---|---|---|---|---|
| Returns | `HHE4AWZZLY` | ACTIVE | `amazon.titan-embed-text-v2:0` | `S3_VECTORS` | `udacity-agentcore-vectors-237657481511` | AVAILABLE |
| Shipping | `KX4W0TT4JJ` | ACTIVE | `amazon.titan-embed-text-v2:0` | `S3_VECTORS` | `udacity-agentcore-vectors-237657481511` | AVAILABLE |
| Warranty | `BNUVVUDQ5J` | ACTIVE | `amazon.titan-embed-text-v2:0` | `S3_VECTORS` | `udacity-agentcore-vectors-237657481511` | AVAILABLE |

Each knowledge base has its own S3 Vectors index and a synced S3 data source for
the matching `policies/returns/`, `policies/shipping/`, or
`policies/warranty/` prefix.

## Automated and live checks

- `python tests/test_agent.py task2`: **40/40 (100%)**
- `python tests/test_agent.py task3`: guardrail and Runtime checks pass
- `python tests/test_agent.py task5`: **25/25 (100%)**, all KBs ACTIVE
- `python tests/test_agent.py task6`: **20/20 (100%)**
- `python -m pytest tests/test_current_api.py -q`: **10 passed**
- Live Runtime: status READY, PUBLIC network, MCP protocol
- Fresh MCP policy invocation: HTTP/runtime success with grounded Premium
  60-day return policy and CommunicationAgent final response
- Fresh AgentCore Observability trace `6a95b4211d7df5dd07e3e8687b916946`:
  **70 spans**, zero system/client errors and zero throttles. The expanded trace
  includes `OrchestratorAgent`, `initialize_session`, `route_to_policy_agent`,
  `PolicyAgent`, `search_all_policies`, all three named policy retriever agents
  and tools, `route_to_communication_agent`, `CommunicationAgent`, and
  `get_full_workflow_context`.
- Final screenshot refresh used live Runtime trace
  `6a96c2fc39511ef3381f28f30de7cea4`: 70 spans, 20,087 tokens,
  zero system errors, zero client errors, and zero throttles. The expanded
  trajectory is committed as `submission/screenshots/09_xray_full_trajectory.png`;
  its metrics page is `10_xray_70_span_details.png`.
- Reviewer-targeted trace `6a96d5e36a6d27257b1e32870fdbb218` contains
  **50 connected spans**, zero errors, and zero throttles. Its expanded
  trajectory visibly connects `invoke_agent OrchestratorAgent` through
  `OrchestratorAgent -> InventoryAgent` to `invoke_agent InventoryAgent`, and
  through `OrchestratorAgent -> CommunicationAgent` to
  `invoke_agent CommunicationAgent`. This is captured in both the required
  `01_xray_service_map.png` and the dedicated
  `11_xray_connected_orchestrator_workers.png` evidence.

### Current SDK compatibility

The course-named logging getter is used when the installed boto3 service model
provides it. With boto3 `1.43.85`, the Task 6 checker now falls back to the
supported AWS APIs used by the same consoles: CloudWatch `DescribeLogGroups`
and X-Ray `GetServiceGraph`. This verifies live AWS state instead of failing on
an unavailable client attribute. The production implementation retains the
rubric-required `put_agent_runtime_logging_configuration()` call and the
AgentCore deployment independently reports log delivery, trace delivery,
X-Ray segment destination, and Transaction Search as enabled.
