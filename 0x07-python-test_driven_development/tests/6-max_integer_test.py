#!/usr/bin/python3
"""Unittest for max_integer
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_unordered_list(self):
        self.assertEqual(max_integer([4, 9, 5, 7]), 9)

    def test_max_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_one_element(self):
        self.assertEqual(max_integer([5]), 5)
