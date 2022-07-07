#!/usr/bin/python3
""" A module containing a single class
    Class:
        -TestInstances
"""
import unittest


class TestInstances(unittest.TestCase):
    """ A class that test data instances'types
        -Args:
            -test_isString(self)
            -test_isInteger(self)
    """
    def test_isString(self):
        """ String tester """
        self.assertEqual(True, isinstance("Test", str))

    def test_isInteger(self):
        """ Integer tester """
        self.assertEqual(True, isinstance(3, int))
