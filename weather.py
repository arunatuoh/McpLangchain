import os
import uvicorn
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str):
    """
    Get weather for a location
    """
    return "it's always raining in Noida"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
