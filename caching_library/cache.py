from enum import Enum, auto
from .eviction_policies.lru_cache import LRU_Cache
from .eviction_policies.lfu_cache import LFU_Cache
from .eviction_policies.fifo_cache import FIFO_Cache
from .eviction_policies.lifo_cache import LIFO_Cache

class EvictionPolicyType(Enum):
    LRU = auto()
    FIFO = auto()
    LIFO = auto()
    LFU = auto()
    
class Cache:
    def __init__(self, capacity, eviction_strategy: EvictionPolicyType):
        self.capacity = capacity
        self.eviction_policy = self.get_policy(eviction_strategy)
        self.cache = {}
    
    def get_policy(self, strategy):
        if strategy == EvictionPolicyType.LRU:
            return LRU_Cache(self.capacity)
        elif strategy == EvictionPolicyType.FIFO:
            return FIFO_Cache(self.capacity)
        elif strategy == EvictionPolicyType.LIFO:
            return LIFO_Cache(self.capacity)
        elif strategy == EvictionPolicyType.LFU:
            return LFU_Cache(self.capacity)
        else:
            raise ValueError("Invalid eviction policy type")
    
    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.eviction_policy.key_accessed(key)
        else:
            if len(self.cache) >= self.capacity:
                evict_key = self.eviction_policy.evict()
                del self.cache[evict_key]
            self.cache[key] = value
            self.eviction_policy.key_accessed(key)

    def get(self, key):
        if key in self.cache:
            self.eviction_policy.key_accessed(key)
            return self.cache[key]
        return None

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        self.cache.clear()
    
    
