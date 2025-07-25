#!/usr/bin/env python3
from typing import List, Union
"""Type annotated function takes a mixed list of integers and floats"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Sums a mixed list
        Args: integers, floats
        Returns: sum of list as floats
    """

    return sum(mxd_lst)
