#!/usr/bin/env python3

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple:
    """
    Calculate the start and end index for a range of items in a paginated list.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index (inclusive) and the end index (exclusive).
    """
    return ((page * page_size) - page_size, page * page_size)
