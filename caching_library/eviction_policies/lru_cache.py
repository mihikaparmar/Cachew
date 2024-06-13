from collections import OrderedDict
from .eviction_policy import EvictionPolicy

class LRU_Cache(EvictionPolicy):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def key_accessed(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            self.cache[key] = None
    
    def evict(self):
        return self.cache.popitem(last=False)[0]
