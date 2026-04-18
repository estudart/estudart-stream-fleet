import asyncio

from src.streamfleet_client.presentation.main import main


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
