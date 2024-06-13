from .eviction_policy import EvictionPolicy

class LIFO_Cache(EvictionPolicy):
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.cache = {}
    
    def key_accessed(self, key):
        if key not in self.stack:
            self.stack.append(key)
    
    def evict(self):
        return self.stack.pop()
