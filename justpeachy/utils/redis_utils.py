import redis

class RedisUtil:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def set(self, key, value):
        """Store a value in Redis."""
        self.client.set(key, value)

    def get(self, key):
        """Retrieve a value from Redis."""
        return self.client.get(key)

    def hset(self, name, mapping):
        """Set multiple hash fields to multiple values."""
        self.client.hset(name, mapping=mapping)

    def hgetall(self, name):
        """Get all fields and values in a hash."""
        return self.client.hgetall(name)

    def delete(self, *names):
        """Delete one or more keys."""
        self.client.delete(*names)
