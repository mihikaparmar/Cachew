from collections import deque
from .eviction_policy import EvictionPolicy

class FIFO_Cache(EvictionPolicy):
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = deque()
        self.cache = {}
    
    def key_accessed(self, key):
        if key not in self.queue:
            self.queue.append(key)
    
    def evict(self):
        return self.queue.popleft()
