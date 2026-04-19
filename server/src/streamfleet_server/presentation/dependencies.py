from typing import Optional

from src.streamfleet_server.application.services.publisher import Publisher
from src.streamfleet_server.infrastructure.redis.redis_adapter import RedisAdapter
from src.streamfleet_server.application.services.consumer import Consumer

_redis_adapter: Optional[RedisAdapter] = None
_publisher: Optional[Publisher] = None
_consumer: Optional[Consumer] = None


def get_redis_adapter() -> RedisAdapter:
    global _redis_adapter
    if _redis_adapter is None:
        _redis_adapter = RedisAdapter()
    return _redis_adapter


def get_publisher() -> Publisher:
    global _publisher
    if _publisher is None:
        _publisher = Publisher(redis_adapter=get_redis_adapter())
    return _publisher

def get_consumer() -> Consumer:
    global _consumer
    if _consumer is None:
        _consumer = Consumer(redis_adapter=get_redis_adapter())
    return _consumer