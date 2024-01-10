#!/usr/bin/python3
"""Module that contains a class student"""


class Student:
    """Attributes:
            first_name: student s first name
            last_name: students last name
            age: students age
    """
    def __init__(self, first_name, last_name, age):
        """initializes class instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of Student"""
        dict_2 = {}
        if isinstance(attrs, list):
            for i in attrs:
                if i in self.__dict__:
                    dict_2[i] = self.__dict__[i]
            return dict_2
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
