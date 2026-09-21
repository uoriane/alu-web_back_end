#!/usr/init/env python3
#!/usr/bin/env python3
"""
This module contains a type-annotated function that returns a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns a float.
    """
    def inner(n: float) -> float:
        return n * multiplier
    return inner
