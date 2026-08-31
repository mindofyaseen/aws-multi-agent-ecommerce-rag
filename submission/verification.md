# Submission verification

Verified on 31 August 2026 in `us-east-1`.

## Automated checks

- InventoryAgent instantiated with exactly 3 tools: PASS
- PolicyAgent instantiated with exactly 1 parallel-search tool: PASS
- OrchestratorAgent instantiated with exactly 5 routing tools: PASS
- Requested Haiku/Sonnet architecture defaults: PASS
- Versioned guardrail exists with content, PII, topic and word policies: PASS
- AgentCore MCP Runtime ARN populated and Runtime status READY: PASS
- Three Knowledge Bases configured, ACTIVE and synced: PASS
- AgentCore SESSION_SUMMARY Memory created with 7-day expiry: PASS (verified
  through the current `bedrock-agentcore-control` API)
- CloudWatch Logs and X-Ray trace delivery: ENABLED by AgentCore deployment

X-Ray API returned two successful live Runtime traces (no error):

```text
1-6a956d68-929d5c0a0e5b9ef633d3fa52  novamart_multi_agent.DEFAULT
1-6a956d43-7a5996658275fda4cf3ccfe1  novamart_multi_agent.DEFAULT
```

## Live MCP test

`tools/list` returned the following deployed tool:

```text
customer_support(message, customer_id="CUST-001", session_id="")
```

Live request:

```text
What is the return policy for Premium customers?
```

Live response began:

```text
The return policy for Premium customers at NovaMart is as follows:
- Return Window: Premium customers have an extended 60-day return window.
```

The response also included grounded eligible/ineligible item rules and completed
with `isError: false`.

## SDK compatibility note

The starter's Task 4/6 assertions target preview operations removed from the
current boto3 service model. They are retained unchanged as course artifacts.
The real resources and delivery setup above were verified using current AWS APIs
and AgentCore deployment output rather than monkey-patching or fabricated data.
