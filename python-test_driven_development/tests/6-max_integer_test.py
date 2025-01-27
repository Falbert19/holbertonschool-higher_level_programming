#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_max_integer_normal(self):
        """Test normal case with a list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_negative(self):
        """Test with a list containing negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_empty(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_max_integer_one_element(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([42]), 42)

    def test_max_integer_float_values(self):
        """Test with a list of float numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_max_integer_mix_int_float(self):
        """Test with a mixed list of integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_max_integer_all_identical(self):
        """Test with a list of identical elements."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_integer_middle(self):
        """Test case where the max integer is in the middle of the list."""
        self.assertEqual(max_integer([1, 5, 3, 2, 4]), 5)


if __name__ == '__main__':
    unittest.main()
