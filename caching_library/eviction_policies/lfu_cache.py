from collections import defaultdict
from .eviction_policy import EvictionPolicy

class LFU_Cache(EvictionPolicy):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.frequency = defaultdict(int)
    
    def key_accessed(self, key):
        self.frequency[key] += 1
    
    def evict(self):
        lfu_key = min(self.frequency, key=self.frequency.get)
        self.frequency.pop(lfu_key)
        return lfu_key
