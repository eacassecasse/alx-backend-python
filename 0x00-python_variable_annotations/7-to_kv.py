#!/usr/bin/env python3
""" This module defines a function to_kv. """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Converts a key and its values into a tuple. """
    return (k, float(v**2))
