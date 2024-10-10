#!/usr/bin/env python3
""" This module defines a function sum_mixed_list. """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Computes the sum of a list of mixed numbers. """
    return float(sum(mxd_lst))
