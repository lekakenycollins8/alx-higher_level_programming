#!/usr/bin/python3
"""Module with a class named Base"""


import json
import os
import csv

class Base:
    """This is the Base class
    Attributes:
        private class attribute: __nb_objects
    Constructor:
        def __init__(self, id=None)
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """initializes class instance
        Args:
            id: class id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation"""
        if list_dictionaries is None or "":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f1:
            j_str = cls.to_json_string([i.to_dictionary() for i in list_objs])
            f1.write(j_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(5, 4)
        elif cls.__name__ == "Square":
            dummy_instance = cls(3)
        else:
            raise ValueError("Unsupported class type")
        dummy_instance.update(**dictionary)
        return dummy_instance
    
    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            file_content = file.read()
        list_of_dicts = cls.from_json_string(file_content)
        instances = [cls.create(**d) for d in list_of_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes instances to CSV file"""
        filename = "{}.csv".format(cls.__name__)

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])
                else:
                    raise ValueError("Unsupported class type")

    @classmethod
    def load_from_file_csv(cls):
        """deserializes instances from CSV file"""
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        instances = []

        with open(filename, mode='r') as file:
            reader = csv.reader(file)

            for row in reader:
                if cls.__name__ == "Rectangle":
                    instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]))
                elif cls.__name__ == "Square":
                    instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
                else:
                    raise ValueError("Unsupported class type")

                instances.append(instance)

        return instances
