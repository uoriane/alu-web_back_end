#!/usr/bin/env python3
"""
This module contains a type-annotated duck-typed iterable function.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable collection of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with each sequence and its integer length.
    """
    return [(i, len(i)) for i in lst]
