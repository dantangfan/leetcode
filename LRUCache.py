from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.items = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not self.items.has_key(key):
            return -1
        value = self.items.pop(key)
        self.items[key] = value
        return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.items.has_key(key):
            self.items.pop(key)
            self.items[key] = value
            return
        if len(self.items) >= self.capacity:
            self.items.popitem(False)
        self.items[key] = value
        
cache = LRUCache( 2 );

cache.put(1, 1);
cache.put(2, 2);
assert 1 == cache.get(1);       # returns 1
cache.put(3, 3);    # evicts key 2
assert -1 == cache.get(2);       # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
assert -1 == cache.get(1);       # returns -1 (not found)
assert 3 == cache.get(3);       # returns 3
assert 4 == cache.get(4);       # returns 4

