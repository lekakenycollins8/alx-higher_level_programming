#!/usr/bin/python3
"""test case for class square"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_constructor_with_valid_arguments(self):
        s = Square(10, 5, 7, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 7)
        self.assertEqual(s.id, 1)

    def test_constructor_with_invalid_arguments(self):
        with self.assertRaises(TypeError):
            s = Square("10", 5, 7, 1)
        with self.assertRaises(ValueError):
            s = Square(-10, 5, 7, 1)
        with self.assertRaises(ValueError):
            s = Square(0, 5, 7, 1)
        with self.assertRaises(ValueError):
            s = Square(10, -5, 7, 1)
        with self.assertRaises(ValueError):
            s = Square(10, 5, -7, 1)

    def test_str_method(self):
        s = Square(10, 5, 7, 1)
        expected_str = "[Square] (1) 5/7 - 10"
        self.assertEqual(str(s), expected_str)

    def test_size_getter_and_setter(self):
        s = Square(10, 5, 7, 1)
        self.assertEqual(s.size, 10)
        s.size = 15
        self.assertEqual(s.size, 15)

        with self.assertRaises(TypeError):
            s.size = "15"

        with self.assertRaises(ValueError):
            s.size = -15

    def test_update_method_with_args(self):
        s = Square(10, 5, 7, 1)
        s.update(2, 15, 8, 10)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 10)

    def test_update_method_with_kwargs(self):
        s = Square(10, 5, 7, 1)
        s.update(id=2, size=15, x=8, y=10)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 10)

    def test_to_dictionary_method(self):
        s = Square(10, 5, 7, 1)
        expected_dict = {'id': 1, 'size': 10, 'x': 5, 'y': 7}
        self.assertEqual(s.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
