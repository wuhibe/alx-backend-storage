#!/usr/bin/env python3
''' Exercise module '''
import redis
import typing
import uuid


class Cache:
    ''' Cache class '''
    def __init__(self):
        ''' initialize Class '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[bytes, int, str, float]) -> str:
        ''' method that stores key-value pairs '''
        id: str = str(uuid.uuid4())
        self._redis.mset({id: data})
        return id

    def get(self, key, fn: typing.Optional[typing.Callable]
            = None) -> typing.Union[bytes, int, str, float]:
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
