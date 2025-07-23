import os
import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import Chatgroq

load_dotenv()


async def main():
    client = MultiServerMCPClient({
        "math": {
            "command": "python3",
            "args": ["mathserver.py"],
            "transport": "stdio",
        },
        "weather": {
            "url": "http://localhost:8001/mcp",
            "transport": "streamable-http",
        },
    })

    tools = await client.get_tools()
    model = Chatgroq(model="qwen-qwq-32b")
    agent = create_react_agent(model, tools)

    try:
        math_response = await agent.ainvoke({"input": "What is 100 + 200?"})
        print("math_response:", math_response['messages'][-1].content)

        weather_response = await agent.ainvoke(
            {"input": "What's the weather in Noida?"})
        print("weather_response:", weather_response['messages'][-1].content)

    except Exception as e:
        print("Error during agent invocation:", e)


if __name__ == "__main__":
    asyncio.run(main())
