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

    def to_json(self):
        """retrieves dictionary representation of Student"""
        return self.__dict__
