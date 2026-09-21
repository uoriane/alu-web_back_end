#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination module
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names (deletion-resilient).
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with deletion-resilient pagination data.
        """
        indexed_data = self.indexed_dataset()
        max_index = max(indexed_data.keys())

        assert index is not None and 0 <= index <= max_index

        data = []
        current_index = index
        items_collected = 0

        while items_collected < page_size and current_index <= max_index:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                items_collected += 1
            current_index += 1

        next_index = current_index if current_index <= max_index else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
