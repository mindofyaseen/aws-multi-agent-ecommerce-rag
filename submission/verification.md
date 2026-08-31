# NovaMart Multi-Agent E-Commerce RAG — Submission Verification

**Region:** `us-east-1`  
**Account ID:** `237657481511`  
**Verification Date:** 31 August 2026  

---

## 1. Automated Test Results

### A. Official Course Test Suite (`tests/test_agent.py`)
```text
Score: 85/120 pts (71%)
```
- **Task 2 (Multi-Agent Orchestration):** PASS (40/40 pts)
  - `build_inventory_agent()` returns Agent with 3 tools: `check_order_status`, `get_customer_tier`, `list_customer_orders`.
  - `build_policy_agent()` returns Agent with 1 parallel tool: `search_all_policies`.
  - `build_orchestrator_agent()` returns Agent with 5 routing tools.
  - Architecture defaults: Claude 3 Haiku (`ORCHESTRATOR_MODEL_ID`), Claude 3 Sonnet (`WORKER_MODEL_ID`).
- **Task 3 (Deployment + Guardrails):** PASS (20/20 pts)
  - Guardrail `udacity-agentcore-guardrail` (`o5xeg6zlw97l` v1) exists and is READY.
  - Content, PII, topic, and profanity policies are fully configured.
  - `AGENTCORE_RUNTIME_ARN` is populated and valid.
- **Task 4 (Memory):** In starter test, calls obsolete preview method `bedrock-agentcore.get_agent_runtime()`. Verified separately via `bedrock-agentcore-control.get_memory`.
- **Task 5 (Bedrock Knowledge Bases):** PASS (25/25 pts)
  - Returns KB (`HHE4AWZZLY`): ACTIVE & Synced
  - Shipping KB (`KX4W0TT4JJ`): ACTIVE & Synced
  - Warranty KB (`BNUVVUDQ5J`): ACTIVE & Synced
- **Task 6 (Observability):** In starter test, calls preview method `get_agent_runtime_logging_configuration()`. Verified via CloudWatch log group and active X-Ray traces.

### B. Modern AWS API Verification Suite (`tests/test_current_api.py`)
```text
Ran 10 tests in 9.461s
OK (100% Passed)
```
- Multi-agent tool registries & model defaults: PASS
- Guardrail status & policies: PASS
- AgentCore Runtime (status `READY`, protocol `MCP`, network `PUBLIC`): PASS
- AgentCore Memory (`ACTIVE`, 7-day retention, `SUMMARIZATION` strategy): PASS
- All three Knowledge Bases (`ACTIVE`): PASS
- CloudWatch log group `/aws/bedrock/agentcore/udacity-agentcore` and X-Ray traces: PASS

Fresh final verification generated X-Ray trace
`1-6a959bd1-6850695b08ae3c0069c94641` from a successful live MCP
policy request (HTTP 200) before running this suite.

---

## 2. Live AgentCore Runtime MCP Verification

**Runtime ARN:** `arn:aws:bedrock-agentcore:us-east-1:237657481511:runtime/novamart_multi_agent-XTb76lG2Mi`  
**Endpoint:** `DEFAULT` (Status: `READY`, Network: `PUBLIC`, Protocol: `MCP`)

### MCP `tools/list`
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "customer_support",
        "description": "Handle one customer-support request using the NovaMart multi-agent graph.",
        "inputSchema": {
          "properties": {
            "message": {"title": "Message", "type": "string"},
            "customer_id": {"default": "CUST-001", "title": "Customer Id", "type": "string"},
            "session_id": {"default": "", "title": "Session Id", "type": "string"}
          },
          "required": ["message"],
          "title": "customer_supportArguments",
          "type": "object"
        },
        "outputSchema": {
          "properties": {"result": {"title": "Result", "type": "string"}},
          "required": ["result"],
          "title": "customer_supportOutput",
          "type": "object"
        }
      }
    ]
  }
}
```

---

## 3. Live Customer Support Scenarios

### Scenario A — Policy Query
- **Message:** `"What is the return policy for Premium customers?"`
- **Customer ID:** `CUST-001`
- **Session ID:** `session-ac121a4a071342b7941b0825908cedcd`
- **HTTP Status:** `200 OK`
- **Output:**
```text
The return policy for Premium customers at NovaMart is as follows:

- Return Window: Premium customers receive an extended 60-day return window. 
- Eligible Items: 
  - Electronics must be in original packaging with all accessories included.
  - Clothing and Footwear must be unworn, unwashed, with original tags attached.
  - Appliances must be unused and in original packaging.
  - Books and Media are eligible for return only if defective.
- Ineligible Items:
  - Perishable goods (food, flowers, plants)
  - Personalized or custom-made items
  - Digital downloads and software licenses
  - Items marked as "Final Sale"
  - Hazardous materials

- Return Process:
  1. Log in to your account and navigate to Order History.
  2. Select the item you wish to return and click "Start Return."
  3. Choose your reason for return from the dropdown menu.
  4. Print the prepaid return shipping label.
  5. Pack the item securely and drop it off at any authorized carrier location.
  6. Refunds are processed within 5-7 business days of receiving the return.
```

### Scenario B — Direct Arithmetic
- **Message:** `"What is 5 * 29.99 * 0.90?"`
- **Customer ID:** `CUST-001`
- **HTTP Status:** `200 OK`
- **Output:**
```text
The result of 5 * 29.99 * 0.90 is 134.955.
```
*(Directly evaluated by OrchestratorAgent without unnecessary specialist routing; rounds to $134.96).*

### Scenario C — Return & Refund Execution
- **Customer ID:** `CUST-003` (Carol Chen, Premium tier)
- **Order ID:** `ORD-35244` (Status: `delivered`, `return_eligible: true`)
- **Message:** `"I want to return my order ORD-35244."`
- **Session ID:** `session-8babf52ec4a643278c2079d4200c6071`
- **HTTP Status:** `200 OK`
- **Output:**
```text
Thank you for reaching out regarding your order ORD-35244. I understand you would like to return it. 

Your order is eligible for return, and the refund process has been initiated. Your return reference is RET-F25168A465. Please use the prepaid return label provided to complete the return process.

If you have any further questions or need assistance, please contact our customer service team at 1-800-NOVAMART. Thank you for your patience and understanding.
```

---

## 4. DynamoDB Optimistic Locking & State Record

DynamoDB Table: `udacity-agentcore-workflow-state`  
ConsistentRead verification for `session-8babf52ec4a643278c2079d4200c6071`:

```json
{
  "session_id": "session-8babf52ec4a643278c2079d4200c6071",
  "customer_id": "CUST-003",
  "created_at": "2026-08-31T12:30:43Z",
  "version": 3,
  "inventory_agent": "The order ORD-35244 is eligible for return. Please contact our customer service team at 1-800-NOVAMART or visit our website for detailed return instructions. Thank you for your patience.",
  "refund_agent": "Your refund for order ORD-35244 has been successfully initiated. Your return reference is RET-F25168A465. Please use the prepaid return label provided to complete the return process. If you have any further questions or need assistance, please contact our customer service team at 1-800-NOVAMART. Thank you for your patience.",
  "communication_agent": "Thank you for reaching out regarding your order ORD-35244. I understand you would like to return it. \n\nYour order is eligible for return, and the refund process has been initiated. Your return reference is RET-F25168A465. Please use the prepaid return label provided to complete the return process.\n\nIf you have any further questions or need assistance, please contact our customer service team at 1-800-NOVAMART. Thank you for your patience and understanding.",
  "ttl": 1788265843
}
```
- **Sequential Version Increments:** `0` -> `1` (Inventory) -> `2` (Refund) -> `3` (Communication).
- **Data Integrity:** All worker findings are preserved; no worker overwrote another worker.

---

## 5. AgentCore Memory Verification

- **Memory ID:** `udacity_agentcore_memory-OBJpmLFy0a`
- **Memory ARN:** `arn:aws:bedrock-agentcore:us-east-1:237657481511:memory/udacity_agentcore_memory-OBJpmLFy0a`
- **Status:** `ACTIVE`
- **Strategy:** `SUMMARIZATION` (`udacity_agentcore_memory_summary`)
- **Event Expiry:** 7 days

Events created and read back via `bedrock-agentcore`:
- Event 1: `0000001788179473199#f4d725d4` | `role: USER` | `"I would like to inquire about returning order ORD-48310."`
- Event 2: `0000001788179475038#2a55f79d` | `role: ASSISTANT` | `"Order ORD-48310 is currently in shipped status and not yet delivered."`

---

## 6. Bedrock Knowledge Bases Grounded Retrieval

All 3 Knowledge Bases verified via `bedrock-agent-runtime.retrieve()`:
1. **Returns KB (`HHE4AWZZLY`):**
   - Query: `"What is the return window for defective electronics?"`
   - Retrieved: `s3://udacity-agentcore-policy-docs-237657481511-d7be52e0/policies/returns/return_policy.txt` (Score: `0.6539`)
2. **Shipping KB (`KX4W0TT4JJ`):**
   - Query: `"How long does standard delivery take?"`
   - Retrieved: `s3://udacity-agentcore-policy-docs-237657481511-d7be52e0/policies/shipping/shipping_policy.txt` (Score: `0.6363`)
3. **Warranty KB (`BNUVVUDQ5J`):**
   - Query: `"What is covered under the 1-year limited warranty?"`
   - Retrieved: `s3://udacity-agentcore-policy-docs-237657481511-d7be52e0/policies/warranty/warranty_policy.txt` (Score: `0.6451`)

---

## 7. Bedrock Guardrail Verification

- **Guardrail ID:** `o5xeg6zlw97l` (Version `1`, Status: `READY`)
- **Safe Request:** `action: NONE` (Passed safely)
- **Harmful / Prohibited Topic Request:** `action: GUARDRAIL_INTERVENED`, `action: BLOCKED`
  - Topics Detected: `legal_threats`, `competitor_products`, `pricing_negotiations`
- **Content Filters:** `SEXUAL` (HIGH), `VIOLENCE` (HIGH), `HATE` (HIGH), `INSULTS` (MEDIUM), `MISCONDUCT` (MEDIUM)
- **PII:** `CREDIT_DEBIT_CARD_NUMBER` (BLOCK), `US_SOCIAL_SECURITY_NUMBER` (BLOCK), `EMAIL` (ANONYMIZE), `PHONE` (ANONYMIZE)
- **Word Policy:** Managed Profanity List enabled

---

## 8. CloudWatch Logs & X-Ray Observability

- **CloudWatch Log Group:** `/aws/bedrock/agentcore/udacity-agentcore` and `/aws/bedrock-agentcore/runtimes/novamart_multi_agent-XTb76lG2Mi-DEFAULT`
- **Active Live Trace IDs on Service `novamart_multi_agent.DEFAULT`:**
  - `1-6a957407-448fd6b623e66f7faa6d7658`
  - `1-6a956f64-b232ce5339c59ee88cdd2302`
  - `1-6a956fe8-8eca8d5f4678aaa6ab44cfb2`
  - `1-6a956fde-cd9dcac98167fe62e8bdc42e`
  - `1-6a956d68-929d5c0a0e5b9ef633d3fa52`
  - `1-6a956d43-7a5996658275fda4cf3ccfe1`
