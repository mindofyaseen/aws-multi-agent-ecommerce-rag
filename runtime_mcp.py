"""MCP entrypoint deployed to Amazon Bedrock AgentCore Runtime."""
import os
import sys
from mcp.server.fastmcp import FastMCP

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from agent_orchestrator import process_request

server = FastMCP("NovaMart Multi-Agent Support", host="0.0.0.0", port=8000,
                 streamable_http_path="/mcp", stateless_http=True, json_response=True)


@server.tool()
def customer_support(message: str, customer_id: str = "CUST-001", session_id: str = "") -> str:
    """Handle one customer-support request using the NovaMart multi-agent graph."""
    return process_request(message, customer_id, session_id or None)


if __name__ == "__main__":
    server.run(transport="streamable-http")
