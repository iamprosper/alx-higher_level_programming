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

    def test_max_at_start(self):
        self.assertEqual(max_integer([9, 5, 6, 8]), 9)

    def test_max_at_end(self):
        self.assertEqual(max_integer([5, 7, 8]), 8)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([5, -9, 6, 4]), 6)

    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-4, -3, -8, -2, -5]), -2)
