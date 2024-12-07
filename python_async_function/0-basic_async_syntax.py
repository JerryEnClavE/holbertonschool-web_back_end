#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    new_func()
    delay = random.uniform(0, max_delay)  # Generate a random float between 0 and max_delay
    await asyncio.sleep(delay)           # Non-blocking wait
    return delay

def new_func():
    """
    Waits for a rand
    Args:
        max_delay (int): Maximum delay in seconds. Default is 10.
    Returns:
        float: The actual delay in seconds.
    """
