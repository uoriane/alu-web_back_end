#!/usr/bin/env python3
"""
This module contains a helper function for pagination index calculation.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return for given pagination parameters.

    Args:
        page (int): Current page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: Start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
