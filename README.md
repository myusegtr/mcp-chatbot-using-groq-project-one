# 🧠 Conversational MCP Agent with Memory (Groq-Powered)

## 🎯 AIM
This project demonstrates a **simple yet powerful chat interface** using `MCPAgent` with built-in conversation memory, powered by a Groq-based LLM. The agent interacts with real-time tools like DuckDuckGo Search, Airbnb listings, and Playwright automation via an MCP (Model Context Protocol) interface.

---

## 📜 Description

This project creates an interactive command-line chat assistant using the `MCPAgent` and a Groq-hosted large language model (LLM). By leveraging MCPClient, it allows the agent to query multiple live data sources like:

- 🔍 **DuckDuckGo Search** for real-time web queries  
- 🏨 **Airbnb** for fetching property listings  
- 🧪 **Playwright** for browser automation and testing workflows  

All tool interactions are defined via a JSON-based configuration (`browser_mcp.json`), and the assistant retains memory during conversation, enabling coherent multi-turn interactions.

### 🛠️ Real-world problem-solving capabilities:

- Trip planning by pulling listings from Airbnb  
- Getting live information via search  
- Automating web-based tasks using Playwright  
- Acting as a smart assistant for customer support, travel, research, or testing automation  

---

## 🧰 Tools & Technologies Used

| Tool / Library             | Purpose                                    |
|---------------------------|--------------------------------------------|
| `langchain_groq`          | Interface to Groq LLMs (e.g., Qwen, LLaMA)  |
| `mcp_use`                 | Manages MCPAgent and MCPClient connections |
| `dotenv`                  | Loads environment variables securely       |
| `asyncio`                 | Handles asynchronous event-driven flow     |
| `browser_mcp.json`        | Configures MCP-compatible server tools     |
| `Cursor Editor`           | Modern, AI-integrated Python IDE used      |
| `npx`                     | Runs MCP server tools via node             |

---

## 📈 Inference / Conclusion

- The combination of Groq's high-speed LLM and MCP's dynamic tooling enables a versatile and responsive agent.
- Memory-enabled agents make the interaction more intelligent and context-aware.
- The abstraction via `MCPClient` and `MCPAgent` significantly simplifies integrating real-world tools into conversational agents.

---

## 🚀 Future Improvements / Enhancements

1. **Web UI Integration**: Replace CLI with a sleek web-based interface using Streamlit or FastAPI.
2. **Tool Extensibility**: Plug in more tools like weather APIs, YouTube search, Google Calendar, etc.
3. **Multimodal Input**: Allow voice or image input for richer user interactions.
4. **Improved Agent Memory**: Persist memory across sessions or store user preferences.
5. **Custom Toolchains**: Design tailored workflows for specific domains like legal research, real estate, or testing.
6. **Chat History Logging**: Store and retrieve previous chats for analysis or training purposes.

This framework serves as a modular foundation for building custom AI agents capable of reasoning, searching, and acting—ideal for prototyping next-gen assistants or domain-specific bots.

---

## ✅ Getting Started

1. Clone the repo.
2. Create `.env` and add your `GROQ_API_KEY`.
3. Ensure Node.js is installed (for MCP tools).
4. Run the app:

```bash
uv run app.py

Note:- Thanks to repo https://github.com/mcptutorial/mcp-use
