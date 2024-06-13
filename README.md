# Cachew: In Memory Cache Library

## Introduction
This library provides an in-memory cache with support for various eviction policies such as Least Recently Used (LRU), Least Frequently Used (LFU), First-In-First-Out (FIFO), and Last-In-First-Out (LIFO). It allows storing key-value pairs in memory and provides methods to retrieve, store, delete items, and clear the cache.

## Exposed Functions

### `get(key)`
Retrieve the value associated with the given key from the cache.

### `put(key, value)`
Store a key-value pair in the cache. If the key already exists, update its value.

### `delete(key)`
Remove the key-value pair from the cache corresponding to the given key.

### `clear()`
Clear the entire cache, removing all key-value pairs.

## Eviction Policies

The library supports the following eviction policies:

### LRU (Least Recently Used)
Evicts the least recently used items first when the cache reaches its maximum capacity.

### LFU (Least Frequently Used)
Evicts the least frequently used items first when the cache reaches its maximum capacity.

### FIFO (First-In-First-Out)
Evicts the oldest items first based on when they were added to the cache.

### LIFO (Last-In-First-Out)
Evicts the most recently added items first.

## Usage Example
To use this library, simply clone this github repository

```python
from cache_library import InMemoryCache, EvictionPolicy

# Create a cache with LRU eviction policy and maximum capacity of 100
cache = InMemoryCache(max_size=100, eviction_policy=EvictionPolicy.LRU)

# Adding items to the cache
cache.put("key1", "value1")
cache.put("key2", "value2")

# Retrieving items from the cache
print(cache.get("key1"))  # Output: value1

# Deleting an item from the cache
cache.delete("key2")

# Clearing the cache
cache.clear()
