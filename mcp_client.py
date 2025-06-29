from mcp_playground import MCPClient
import asyncio

async def main():
    client = MCPClient("http://127.0.0.1:8000/sse")

    res = await client.invoke_tool("/fetch_history", {"profile_number": "1"})

    print(res.content['text'])

asyncio.run(main())
