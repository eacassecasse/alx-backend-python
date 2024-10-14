#!/usr/bin/env python3
""" This module defines a wait_random function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random number of seconds. """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time