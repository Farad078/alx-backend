#!/usr/bin/python3
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return None
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
