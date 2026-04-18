import asyncio

from src.streamfleet_client.presentation.dependencies import get_computer_streamer


async def main():
    streamer = get_computer_streamer()
    await streamer.start_streaming()


if __name__ == "__main__":
    asyncio.run(main())
