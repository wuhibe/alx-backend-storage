#!/usr/bin/env python3
''' Exercise module '''
import redis
import typing
import uuid


class Cache:
    def __init__(self):
        ''' initialize Class '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Any) -> str:
        ''' method that stores key-value pairs '''
        id: str = str(uuid.uuid4())
        self._redis.mset({id: data})
        return id

    def get(self, key, fn: typing.Callable = None) -> typing.Any:
        ''' getter method for stored pairs '''
        val: bytes = self._redis.get(key)
        if fn is not None:
            val = fn(val)
        return val
