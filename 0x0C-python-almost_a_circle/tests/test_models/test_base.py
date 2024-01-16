#!/usr/bin/python3
"""Defines unittests for base.py.

"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_constructor_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_constructor_with_mixed_id_and_no_id(self):
        obj1 = Base(id=10)
        obj2 = Base()
        obj3 = Base(id=15)
        self.assertEqual(obj1.id, 10)
        self.assertEqual(obj2.id, 1)
        self.assertEqual(obj3.id, 15)
    def test_to_json_string_with_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_with_none_list(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_with_valid_list(self):
        input_list = [
            {"id": 1, "name": "object1"},
            {"id": 2, "name": "object2"},
            {"id": 3, "name": "object3"}
        ]
        expected_result = '[{"id": 1, "name": "object1"}, {"id": 2, "name": "object2"}, {"id": 3, "name": "object3"}]'
        result = Base.to_json_string(input_list)
        self.assertEqual(result, expected_result)

    def test_to_json_string_with_mixed_types(self):
        input_list = [
            {"id": 1, "name": "object1"},
            None,
            {"id": 2, "name": "object2"},
            {"id": 3, "name": "object3"}
        ]
        expected_result = '[{"id": 1, "name": "object1"}, null, {"id": 2, "name": "object2"}, {"id": 3, "name": "object3"}]'
        result = Base.to_json_string(input_list)
        self.assertEqual(result, expected_result)

    def test_from_json_string_with_empty_string(self):
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_with_none_string(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_with_valid_json_string(self):
        json_string = '[{"id": 1, "name": "object1"}, {"id": 2, "name": "object2"}, {"id": 3, "name": "object3"}]'
        expected_result = [
            {"id": 1, "name": "object1"},
            {"id": 2, "name": "object2"},
            {"id": 3, "name": "object3"}
        ]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected_result)

    def test_from_json_string_with_invalid_json_string(self):
        json_string = '{"id": 1, "name": "object1"}'  # Not a list
        with self.assertRaises(json.JSONDecodeError):
            Base.from_json_string(json_string)
    
    def test_create_with_rectangle(self):
        dummy_instance = Base.create(width=10, height=20, id=5)
        self.assertEqual(dummy_instance.id, 5)
        self.assertEqual(dummy_instance.width, 10)
        self.assertEqual(dummy_instance.height, 20)

    def test_create_with_square(self):
        dummy_instance = Base.create(size=15, id=7)
        self.assertEqual(dummy_instance.id, 7)
        self.assertEqual(dummy_instance.size, 15)

    def test_load_from_file_with_nonexistent_file(self):
        filename = "NonExistentClass.json"
        self.assertFalse(os.path.isfile(filename))
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_with_existing_file(self):
        filename = "Rectangle.json"
        dummy_instance = Rectangle(width=10, height=20, id=1)
        dummy_instance.save_to_file(filename)
        self.assertTrue(os.path.isfile(filename))
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 1)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].width, 10)
        self.assertEqual(instances[0].height, 20)
        os.remove(filename)

    def test_save_to_file_csv_with_empty_list(self):
        filename = "Rectangle.csv"
        Rectangle.save_to_file_csv([])
        self.assertTrue(os.path.isfile(filename))

        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, "")

        os.remove(filename)

    def test_save_to_file_csv_with_valid_list(self):
        filename = "Rectangle.csv"
        instances = [Rectangle(id=1, width=10, height=20, x=5, y=7),
                     Rectangle(id=2, width=15, height=25, x=8, y=10)]

        Rectangle.save_to_file_csv(instances)
        self.assertTrue(os.path.isfile(filename))

        with open(filename, 'r') as file:
            content = file.read()
            expected_content = "1,10,20,5,7\n2,15,25,8,10\n"
            self.assertEqual(content, expected_content)

        os.remove(filename)

    def test_load_from_file_csv_with_nonexistent_file(self):
        filename = "NonExistentClass.csv"
        self.assertFalse(os.path.isfile(filename))
        instances = Base.load_from_file_csv()
        self.assertEqual(instances, [])

    def test_load_from_file_csv_with_existing_file(self):
        filename = "Rectangle.csv"
        content = "1,10,20,5,7\n2,15,25,8,10\n"

        with open(filename, 'w') as file:
            file.write(content)

        self.assertTrue(os.path.isfile(filename))
        instances = Rectangle.load_from_file_csv()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].width, 10)
        self.assertEqual(instances[0].height, 20)
        self.assertEqual(instances[0].x, 5)
        self.assertEqual(instances[0].y, 7)
        self.assertIsInstance(instances[1], Rectangle)
        self.assertEqual(instances[1].id, 2)
        self.assertEqual(instances[1].width, 15)
        self.assertEqual(instances[1].height, 25)
        self.assertEqual(instances[1].x, 8)
        self.assertEqual(instances[1].y, 10)

        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
