import unittest
from caching_library.cache import Cache, EvictionPolicyType  # Assuming the Cache class and EvictionPolicyType enum are in a file named cache.py

class TestCache(unittest.TestCase):
    
    def test_lru_cache(self):
        cache = Cache(capacity=3, eviction_strategy=EvictionPolicyType.LRU)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        self.assertEqual(cache.get("a"), 1)  # Access "a" to make it most recently used
        cache.put("d", 4)  # Should evict "b" (least recently used)
        self.assertDictEqual(cache.cache, {"c": 3, "a": 1, "d": 4})
        
        # Test delete
        cache.delete("a")
        self.assertDictEqual(cache.cache, {"c": 3, "d": 4})
        
        # Test clear
        cache.clear()
        self.assertDictEqual(cache.cache, {})
    
    def test_fifo_cache(self):
        cache = Cache(capacity=3, eviction_strategy=EvictionPolicyType.FIFO)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        cache.put("d", 4)  # Should evict "a" (first in)
        self.assertDictEqual(cache.cache, {"b": 2, "c": 3, "d": 4})
        
        # Test delete
        cache.delete("b")
        self.assertDictEqual(cache.cache, {"c": 3, "d": 4})
        
        # Test clear
        cache.clear()
        self.assertDictEqual(cache.cache, {})
    
    def test_lifo_cache(self):
        cache = Cache(capacity=3, eviction_strategy=EvictionPolicyType.LIFO)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        cache.put("d", 4)  # Should evict "c" (last in before "d")
        self.assertDictEqual(cache.cache, {"a": 1, "b": 2, "d": 4})
        
        # Test delete
        cache.delete("b")
        self.assertDictEqual(cache.cache, {"a": 1, "d": 4})
        
        # Test clear
        cache.clear()
        self.assertDictEqual(cache.cache, {})
    
    def test_lfu_cache(self):
        cache = Cache(capacity=3, eviction_strategy=EvictionPolicyType.LFU)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        cache.get("a")  # Access "a" to increase its frequency
        cache.get("a")  # Access "a" to increase its frequency
        cache.put("d", 4)  # Should evict "b" or "c" (least frequently used)
        
        # Check if either "b" or "c" is evicted
        self.assertIn("a", cache.cache)
        self.assertIn("d", cache.cache)
        self.assertEqual(len(cache.cache), 3)
        
        # Test delete
        cache.delete("a")
        self.assertNotIn("a", cache.cache)
        
        # Test clear
        cache.clear()
        self.assertDictEqual(cache.cache, {})

if __name__ == "__main__":
    unittest.main()
