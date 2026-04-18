from src.streamfleet_server.infrastructure.redis.redis_adapter import RedisAdapter


class Publisher:
    """Application service: publish text payloads to Redis channels (e.g. base64 JPEG from clients)."""

    def __init__(self, redis_adapter: RedisAdapter):
        self._redis = redis_adapter

    def publish(self, channel: str, message: str) -> bool:
        try:
            self._redis.publish(channel=channel, message=message)
            return True
        except Exception as err:
            print(f"Redis publish failed: {err}")
            return False