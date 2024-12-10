import asyncio
import random

async def async_generator():
    """

    Coroutine that yeilds a random number between 0 and 10,
    after asynchronously wathing for 1 second, repeted 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1) # Asynchronusly wait for 1 second
        yield random.uniform(0, 10) # Genereate a random float between 0 and 10

