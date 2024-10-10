#!/usr/bin/env python3
""" This module defines a function make_multiplier. """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Computes a multiplication. """
    return lambda x: x * multiplier
