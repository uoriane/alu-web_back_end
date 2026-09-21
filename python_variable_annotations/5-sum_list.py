#!/usr/bin/env python3
"""
This module contains a type-annotated function to sum a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Take a list of floats and return their sum as a float.

    Args:
        input_list (List[float]): List of floating-point numbers.

    Returns:
        float: The sum of the list elements.
    """
    return sum(input_list)
