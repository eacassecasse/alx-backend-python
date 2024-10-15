#!/usr/bin/env python3
""" This module defines a coroutine called async_comprehension. """

from typing import List
from importlib import import_module as use

async_generator = use('0-async_generator').async_generator


async def async_comprehension():
    """ Creates a list of 10 random numbers using a generator. """
    result = [i async for i in async_generator()]
    return result
