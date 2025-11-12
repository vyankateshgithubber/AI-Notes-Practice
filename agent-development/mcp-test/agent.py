
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise RuntimeError("Missing required environment variable: GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.gemma_llm import Gemini
from google.adk.runners import InMemoryRunner

mcp_image_server = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-everything"
            ],
            tool_filter=["getTinyImage"]
        ),
        timeout=30
    )
)


image_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite"),
    name="image_agent",
    instruction="Use the MCP Tool to generate images for user queries",
    tools=[mcp_image_server],
)


runner = InMemoryRunner(agent=image_agent)

async def run_agent():
    response = await runner.run_debug("Provide a sample tiny image", verbose=True)
    print("Agent Response:", response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_agent())