#!/usr/bin/env python3
""" This module defines a function element_length. """

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Computes the length of a list of sequences. """
    return [(i, len(i)) for i in lst]
