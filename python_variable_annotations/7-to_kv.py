#!/usr/bin/env python3
"""
This module contains a type-annotated function that returns a tuple
containing a string and the square of an int/float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with string k and the square of v as a float.

    Args:
        k (str): A string element.
        v (Union[int, float]): An integer or float to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is k and the second is v squared.
    """
    return (k, float(v ** 2))
