#!/usr/bin/env python3
''' Exercise module '''
from functools import wraps
from typing import Union, Optional, Callable
import redis
import uuid


def count_calls(fn: Callable) -> Callable:
    ''' counter for number of calls to Cache class '''
    key = fn.__qualname__

    @wraps(fn)
    def wrapper(self, *args, **kwds):
        ''' method to call decorated fn '''
        self._redis.incr(key)
        return fn(self, *args, **kwds)
    return wrapper


class Cache:
    ''' Cache class '''
    def __init__(self):
        ''' initialize Class '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' method that stores key-value pairs '''
        id: str = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key, fn: Optional[Callable]
            = None) -> Union[bytes, int, str, float]:
        ''' getter method for stored pairs '''
        val: bytes = self._redis.get(key)
        if fn is not None:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        ''' getter for str '''
        return self._redis.get(key, str)

    def get_int(self, key: str) -> int:
        ''' getter for int '''
        return self._redis.get(key, int)
