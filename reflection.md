# Reflection

The most important design decision was to keep coordination state outside the
language models. Each specialist writes its result to one DynamoDB
`WorkflowState` record, and every update includes an expected version. This
optimistic-locking approach makes the orchestration auditable and prevents two
parallel workers from silently overwriting one another. It also keeps worker
prompts focused: inventory retrieves facts, policy performs grounded retrieval,
refund makes a bounded decision, and communication writes for the customer.

The main challenge was the gap between the course's preview AgentCore API and
the current AWS SDK. The provided tests reference runtime-attached memory and
logging methods that are no longer present in boto3 1.43.83. I resolved this by
using the current control-plane APIs: an independent SESSION_SUMMARY memory with
seven-day retention, and the AgentCore deployment toolkit's real CloudWatch and
X-Ray delivery configuration. I deliberately did not monkey-patch missing SDK
operations. A second account constraint blocked Anthropic invocation until a
use-case form is submitted, so the deployed Runtime uses Amazon Nova models via
environment overrides while retaining the requested model architecture as the
code default.

For production, I would add authenticated customer identity rather than accept
customer IDs from request text, apply least-privilege IAM per worker, encrypt
and minimize state retention, and require idempotency keys plus human approval
for high-value refunds. I would also add offline retrieval evaluation, prompt
regression tests, per-agent latency/cost alarms, dead-letter handling, and a
review queue for low-confidence policy conflicts. Guardrail outcomes, tool
calls, KB citations, state version conflicts, and customer-visible decisions
would be correlated through one trace ID for operational investigation.
