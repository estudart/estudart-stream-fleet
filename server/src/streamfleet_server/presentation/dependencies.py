from typing import Optional

from src.streamfleet_server.application.services.publisher import Publisher
from src.streamfleet_server.infrastructure.redis.redis_adapter import RedisAdapter

_redis_adapter: Optional[RedisAdapter] = None
_publisher: Optional[Publisher] = None


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