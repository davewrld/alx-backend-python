#!/usr/bin/env python3
"""Mixed type annoted function of string
    and int/float to tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """"Returns a tuple of string and int/float square

    Args:
        k: str
        v: int/float

    Returns:
        Tuple(k, v-square)
    """

    return (k, v**2)
