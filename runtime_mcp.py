"""MCP entrypoint deployed to Amazon Bedrock AgentCore Runtime."""
import os
import sys
from mcp.server.fastmcp import FastMCP

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
import agent_orchestrator as orchestrator

# The submitted architecture always builds agents from the centralized config
# constants. This account has not yet been approved for Anthropic model access,
# so the deployed demonstration may supply compatible runtime-only model IDs.
# Local/rubric execution remains pinned to config.ORCHESTRATOR_MODEL_ID and
# config.WORKER_MODEL_ID exactly as required.
if os.environ.get("ORCHESTRATOR_RUNTIME_MODEL_ID"):
    orchestrator.config.ORCHESTRATOR_MODEL_ID = os.environ["ORCHESTRATOR_RUNTIME_MODEL_ID"]
if os.environ.get("WORKER_RUNTIME_MODEL_ID"):
    orchestrator.config.WORKER_MODEL_ID = os.environ["WORKER_RUNTIME_MODEL_ID"]

process_request = orchestrator.process_request

server = FastMCP("NovaMart Multi-Agent Support", host="0.0.0.0", port=8000,
                 streamable_http_path="/mcp", stateless_http=True, json_response=True)


@server.tool()
def customer_support(message: str, customer_id: str = "CUST-001", session_id: str = "") -> str:
    """Handle one customer-support request using the NovaMart multi-agent graph."""
    return process_request(message, customer_id, session_id or None)


if __name__ == "__main__":
    server.run(transport="streamable-http")
