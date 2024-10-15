#!/usr/bin/env python3
""" This module defines a coroutine called async_comprehension. """

import asyncio
import time
from importlib import import_module as use

async_comprehension = use('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ Measures the runtime of async_comprehension. """
    s = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - s
