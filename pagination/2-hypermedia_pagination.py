#!/usr/bin/env python3
"""
This module contains a Server class with hypermedia pagination support.
"""
import csv
import math
from typing import List, Dict, Any

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names with hypermedia.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary containing hypermedia pagination details.
        """
        data = self.get_page(page, page_size)
        total_dataset_length = len(self.dataset())
        total_pages = math.ceil(total_dataset_length / page_size) if page_size > 0 else 0

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Handle edge case where requested page is out of range
        if not data and page > total_pages:
            page_size = 0

        return {
            "page_size": page_size if data or page <= total_pages else 0,
            "page": page,
            "data": data,
            "next_page": next_page if data else None,
            "prev_page": prev_page if page <= total_pages and page > 1 else (prev_page if data else None),
            "total_pages": total_pages
        }
