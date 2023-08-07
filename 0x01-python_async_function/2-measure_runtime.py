#!/usr/bin/env python3
'''Measure the runtime module'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int = 0, max_delay: int = 10) -> float:
    '''Measures the total execution time for wait_n(n, max_delay), and returns
       total_time / n. Your function should return a float.'''
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()
    return (end - start) / n
