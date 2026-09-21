#!/usr/bin/env python3
"""
This module contains a type-annotated function to return the floor of a float.
"""
import math


def floor(n: float) -> int:
    """
    Return the floor of the float argument.

    Args:
        n (float): The floating-point number to floor.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
