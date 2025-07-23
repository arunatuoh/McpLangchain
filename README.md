# MCP LangChain Integration Project

A Model Context Protocol (MCP) implementation with multiple servers and LangChain integration for AI agent interactions.

## 🚀 Project Overview

This project demonstrates how to create MCP servers and integrate them with LangChain agents using the GROQ API. It includes:

- **Weather Server**: A simple weather service that returns weather information
- **Math Server**: A mathematical operations service with add and multiply functions
- **Client**: A LangChain agent that can interact with both servers

## 📁 Project Structure

```
MCPLangchain/
├── weather.py          # Weather MCP server
├── mathserver.py       # Math MCP server  
├── client.py           # LangChain client with agent
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (API keys)
└── README.md          # This file
```

## 🛠️ Installation

1. **Clone and setup the environment:**
```bash
cd MCPLangchain
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
Create a `.env` file with your GROQ API key:
```
GROQ_API_KEY="your_groq_api_key_here"
```

## 🏃‍♂️ Running the Project

### 1. Start the Weather Server
```bash
python weather.py
```
The weather server will start on port 8001 with streamable-http transport.

### 2. Start the Math Server (in a separate terminal)
```bash
python mathserver.py
```
The math server uses stdio transport for direct communication.

### 3. Run the Client
```bash
python client.py
```
This will:
- Connect to both MCP servers
- Create a LangChain agent with GROQ model
- Execute math and weather queries

## 🔧 Configuration

### Weather Server (`weather.py`)
- **Transport**: streamable-http
- **Port**: 8000
- **Function**: `get_weather(location)` - Returns weather info for any location

### Math Server (`mathserver.py`)
- **Transport**: stdio
- **Functions**: 
  - `add(a, b)` - Adds two integers
  - `multiply(a, b)` - Multiplies two integers

### Client (`client.py`)
- **Model**: GROQ Qwen-QWQ-32B
- **Agent Type**: React Agent
- **Capabilities**: Can invoke tools from both servers

## 📋 Dependencies

- `mcp` - Model Context Protocol implementation
- `langchain-mcp-adapters` - LangChain MCP integration
- `langchain-groq` - GROQ API integration
- `langgraph` - LangGraph for agent creation
- `uvicorn` - ASGI server for HTTP transport
- `python-dotenv` - Environment variable management

## 🎯 Example Usage

The client demonstrates two main interactions:

1. **Math Operations**: "What is 100 + 200?"
2. **Weather Queries**: "What's the weather in Noida?"

### Import Errors
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### API Key Issues
Verify your `.env` file contains the correct GROQ API key:
```
GROQ_API_KEY="gsk_your_actual_key_here"
```

## 🚀 Next Steps

- Add more MCP servers (database, file system, etc.)
- Implement more complex agent workflows
- Add authentication and security features
- Create a web interface for the agent

## 📚 Resources

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [GROQ API Documentation](https://console.groq.com/docs)

---

**Note**: This project demonstrates the power of MCP for creating modular, composable AI services that can be easily integrated with LangChain agents.
