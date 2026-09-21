#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return it.

    Args:
        max_delay (int): Maximum delay limit (default 10).

    Returns:
        float: The random delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
