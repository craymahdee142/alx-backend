#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class that inherit from BaseCache, it is a caching system.
    It does not have limit
    """

    def __init__(self):
        """
        Initialize the class using parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Assigned to a dcitionary"""
        if key is None and item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value linked to key
        if key is none, and deos not exist return none
        """
        if key is None and self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
