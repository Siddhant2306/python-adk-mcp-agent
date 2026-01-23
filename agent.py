import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams
from dotenv import load_dotenv

load_dotenv()

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="remote_mcp_assistant",
    instruction="Use the connected remote tools to assist the user.",
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url=os.getenv("MCP_SERVER_URL")
            )
        ),
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url= os.getenv("SEQUENTIAL_MCP_URL")
            )
        )
    ]
)
