#!/usr/bin/env python3

import asyncio
import random

"""asynchronous coroutine program
prints random delay
"""


async def wait_random(max_delay: int = 10) -> float:
    """waits a random delay between 0 -10.
    Args:
        int: max_delay.

    Returns:
        float: Delay in seconds
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
