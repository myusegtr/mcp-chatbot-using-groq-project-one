import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables from .env
    load_dotenv()

    # Get Groq API key from environment
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY is not set in your environment")

    # Create MCPClient from config file
    config_path = os.path.join(os.path.dirname(__file__), "browser_mcp.json")
    client = MCPClient.from_config_file(config_path)

    # Create Groq LLM
    llm = ChatGroq(model_name="qwen-qwq-32b", api_key=groq_api_key)

    # Create MCPAgent
    agent = MCPAgent(llm=llm, client=client, max_steps=5)
    
    print("Interacting MCP agent")
    print("Type 'exit' or 'quit' to end the conversation")

    # Run a query through the agent
    try:
        while True:
            user_input = input("Enter a query: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting the conversation")
                break
                
            print("\nAssistant: ", end="", flush=True)

            try:
                result = await agent.run(user_input)
                print(f"\nResult: {result}")
            except Exception as e:
                print(f"\nError: {e}")
    finally:
        if client and client.session:
            await client.session.close()
   



if __name__ == "__main__":
    asyncio.run(main())
