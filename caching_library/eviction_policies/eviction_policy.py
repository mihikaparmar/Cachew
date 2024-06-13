from abc import ABC, abstractmethod

class EvictionPolicy(ABC):
    def __init__(self, capacity):
        self.capacity = capacity
    
    @abstractmethod
    def key_accessed(self, key):
        pass
    
    @abstractmethod
    def evict(self):
        pass
