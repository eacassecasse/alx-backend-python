#!/usr/bin/env python3
""" This module defines a function sum_list. """

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """ Computes the sum of a list of floating-point numbers. """
    total: float = 0
    for el in input_list:
        total += el
    return total
