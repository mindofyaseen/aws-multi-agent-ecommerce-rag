# Fresh AWS CLI Verification — 2026-09-01

This report records a read-only verification performed against the live AWS
resources in `us-east-1` immediately before packaging the resubmission.

## Knowledge Bases

The following command was run separately for each Knowledge Base:

```powershell
aws bedrock-agent get-knowledge-base `
  --knowledge-base-id <KB_ID> `
  --region us-east-1
```

| Knowledge Base | ID | Status | Storage | Vector index | Embedding model |
|---|---|---|---|---|---|
| `novamart-returns-policy-kb` | `HHE4AWZZLY` | `ACTIVE` | `S3_VECTORS` | `novamart-returns-index` | `amazon.titan-embed-text-v2:0` |
| `novamart-shipping-policy-kb` | `KX4W0TT4JJ` | `ACTIVE` | `S3_VECTORS` | `novamart-shipping-index` | `amazon.titan-embed-text-v2:0` |
| `novamart-warranty-policy-kb` | `BNUVVUDQ5J` | `ACTIVE` | `S3_VECTORS` | `novamart-warranty-index` | `amazon.titan-embed-text-v2:0` |

All three configurations returned this S3 Vectors bucket ARN:

```text
arn:aws:s3vectors:us-east-1:237657481511:bucket/udacity-agentcore-vectors-237657481511
```

This directly addresses the reviewer requirement to verify the Returns,
Shipping, and Warranty S3 Vectors backing stores.

## X-Ray service graph

`aws xray get-service-graph` returned:

- Service `novamart_multi_agent.DEFAULT` in `active` state.
- A client node for `novamart_multi_agent.DEFAULT`.
- A successful client edge with `OkCount: 3`, `TotalCount: 3`, zero errors,
  zero faults, and zero throttles.
- The service graph also contained AWS STS and CloudFormation dependencies.

The newer expanded AgentCore Observability trace is documented in
`xray_trace_results.md`: trace `6a95b4211d7df5dd07e3e8687b916946`
contains 70 spans and the complete Orchestrator, specialist, policy-retriever,
and CommunicationAgent execution chain.

## Automated checks

Run with the repository virtual environment and `PYTHONUTF8=1`:

- Task 2: `40/40` (100%).
- Task 3: `20/20` (100%).
- Task 5: `25/25` (100%); all three Knowledge Bases ACTIVE.
- Python compilation: successful for `src/agent_orchestrator.py` and
  `runtime_mcp.py`.

Task 4 and Task 6 course checks currently call boto3 methods that are absent
from the installed boto3 `1.43.83` service models. This SDK compatibility issue
and the independently verified live resources are explained in
`resubmission_fixes.md`.

