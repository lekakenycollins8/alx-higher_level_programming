#!/usr/bin/python3
"""test cases for class rectangle"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_constructor_with_valid_arguments(self):
        r = Rectangle(10, 20, 5, 7, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 7)
        self.assertEqual(r.id, 1)

    def test_constructor_with_invalid_arguments(self):
        with self.assertRaises(TypeError):
            r = Rectangle("10", 20, 5, 7, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 20, 5, 7, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 0, 5, 7, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -5, 7, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 5, -7, 1)

    def test_area_method(self):
        r = Rectangle(10, 20, 5, 7, 1)
        self.assertEqual(r.area(), 200)

    def test_display_method(self):
        r = Rectangle(3, 2, 0, 0, 1)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_method(self):
        r = Rectangle(10, 20, 5, 7, 1)
        expected_str = "[Rectangle] (1) 5/7 - 10/20"
        self.assertEqual(str(r), expected_str)

    def test_update_method_with_args(self):
        r = Rectangle(10, 20, 5, 7, 1)
        r.update(2, 15, 25, 8, 10)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 10)

    def test_update_method_with_kwargs(self):
        r = Rectangle(10, 20, 5, 7, 1)
        r.update(id=2, width=15, height=25, x=8, y=10)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 10)

    def test_to_dictionary_method(self):
        r = Rectangle(10, 20, 5, 7, 1)
        expected_dict = {'id': 1, 'width': 10, 'height': 20, 'x': 5, 'y': 7}
        self.assertEqual(r.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
