# Implement a Least Recently Used (LRU) cache counter that tracks how many times each key is accessed. Support get(key) and put(key) operations with a fixed capacity.

class LRUCacheCounter:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key: count
    
    def get(self, key):
        pass
    
    def put(self, key):
        pass

lru = LRUCacheCounter(2)
lru.put(1)
lru.put(2)
lru.get(1)
lru.put(3)
print(lru.cache)
