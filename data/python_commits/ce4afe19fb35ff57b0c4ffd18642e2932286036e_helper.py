class RedisClient:
    """Redis client class."""

    def __init__(self):
        self.redis = None

    def get_client(self):
        if not self.redis:
            self.redis = self.get_redis()
        return self.redis
    
    def get_redis(self):
        """Get the Redis client."""
        try:
            redis_client = Redis(host=os_environ.get("REDIS_HOST", "redis"),
                                port=int(os_environ.get("REDIS_PORT", 6379)),
                                db=int(os_environ.get("REDIS_DB", 0)),
                                password=os_environ.get("REDIS_PASSWORD", None),
                                decode_responses=True)
            redis_client.ping()
            return redis_client
        except ConnectionError as e:
            print(f"Redis connection error: {e}")
            raise RuntimeError("Redis server is not reachable.")
    
    def ping(self):
        """Ping the Redis server."""
        try:
            self.redis.ping()
            return True
        except ConnectionError as e:
            print(f"Redis connection error: {e}")
            return False

