#!?usr/bin/env python3
'''type-annotated module for to_kv function'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''takes a string k and an int OR float v as arguments
    returns a tuple
    '''
    return (k, v ** 2)