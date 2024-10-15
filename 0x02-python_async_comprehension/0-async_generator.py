#!/usr/bin/env python3
""" This module defines a coroutine called async_generator. """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Generates 10 numbers asynchronously. """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
