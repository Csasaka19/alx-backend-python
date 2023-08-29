#!/usr/bin/env python3
'''Test functionality of utils module'''
import unittest
from utils import access_nested_map
from typing import Union, Tuple, Dict
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''Test class for access_nested_map in utils.py'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            path: Tuple[str],
            nested_map: Dict,
            expected: Union[Dict, int],
            ) -> None:
        '''test output method'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """test access_nested_map exception raising method"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
