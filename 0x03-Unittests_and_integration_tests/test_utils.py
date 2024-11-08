#!/usr/bin/env python3
"""Parameterize unittest"""


import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Base test for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test successful cases"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """Test exception cases"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
