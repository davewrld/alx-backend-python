#!/usr/bin/env python3
"""Type annotated function takes a mixed list
    of integers and floats
    """


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a mixed list of floats and integers..

    Args:
        mxd_lst (List[int, float): list of integers and floats.

    Returns:
        float: Sum all numbers in mxd_lst.
    """

    return sum(mxd_lst)
