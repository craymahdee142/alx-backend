#!/usr/bin/env python3
"""FIFO Caching"""
from base_caching import BaseCaching


clas LIFOCache(BaseCaching):
    """
    LIFO Caching for caching system
    """

    def __init__(self):
        """
        Initialize with parent class method super init
        """
        super.__init__()
        self.order = []

    def put(self, key, item):
        """Assign to a dictionary"""
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key is not self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                def self.order[-1]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, get):
        """Return the value linked to a given key or None"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
