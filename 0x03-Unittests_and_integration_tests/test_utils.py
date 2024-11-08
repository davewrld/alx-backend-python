#!/usr/bin/env python3
"""Module utils"""

import unittest
from unittest.mock import MagicMock, patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """base test for access_nested_map function"""

    @parameterized.expand([
        {"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test succesful cases"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
