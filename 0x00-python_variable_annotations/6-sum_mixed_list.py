#!/usr/bin/env python3
"""Mixed list module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of a list of floats and integers"""
    return float(sum(mxd_lst))