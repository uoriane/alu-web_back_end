#!/usr/bin/env python3
"""
This module contains a type-annotated function to sum a list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Take a list of integers and floats and return their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): List containing integers and floats.

    Returns:
        float: The sum of all elements in the list.
    """
    return float(sum(mxd_lst))
