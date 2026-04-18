import asyncio

from src.streamfleet_client.presentation.dependencies import get_websocket_consumer


async def main():
    wss = get_websocket_consumer("4856177744")
    async for payload in wss.get_messages():
        preview = payload[:72] + "..." if len(payload) > 72 else payload
        print(f"{len(payload)} chars: {preview}")

def run():
    asyncio.run(main())

if __name__ == "__main__":
    run()
