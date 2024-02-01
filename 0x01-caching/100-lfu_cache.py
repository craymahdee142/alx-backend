#!/usr/bin/env python3
"""FIFO Caching"""
from base_caching import BaseCaching


clas LFUCache(BaseCaching):
    """
    LFU Caching for caching system
    """

    def __init__(self):
        """
        Initialize with parent class method super init
        """
        super.__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """Assign to a dictionary"""
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key is not self.cache_data:
                lfu = min(self.frequency.values())
                lfu_keys = []
                for k, v in self.frequency.items():
                    if v == lfu:
                        lfu_keys.append(k)
                if len(lfu_keys) > 1:
                    lru_lfu = {}
                    for k in lfu_keys:
                        lfu_lfu[k] = self.usage.index(k)
                    discard = min(lru_lfu.values())
                    discard = self.usage[discard]
                else:
                    discard = lfu_keys[0]

                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[discard]
                def self.usage[self.usage.index(discard)]
                def self.frequency[discard]
            # Update usage frequency
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.usage:
                def self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, get):
        """Return the value linked to a given key or None"""
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None