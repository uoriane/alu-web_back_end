#!/usr/bin/env python3
"""
This module measures the runtime of wait_n.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total execution time for wait_n(n, max_delay) and return total_time / n.

    Args:
        n (int): Number of coroutines.
        max_delay (int): Maximum delay.

    Returns:
        float: Average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
