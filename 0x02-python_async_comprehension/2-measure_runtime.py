#!/usr/bin/env python3
""" Async parallel Comprehensions module"""
import time
import asyncio


asyncio_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Async parallel Comprehensions module"""
    start = time.time()
    await asyncio.gather(*(asyncio_comprehension() for i in range(4)))
    end = time.time()
    return end - start
