#!/usr/bin/env python3
"""Serialization"""
import pickle


class CustomObject:
    """customobject for task"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(
            "Name: {}\nAge: {}\nIs Student: {}".format(
                self.name, self.age, self.is_student
            ),
            end="",
        )

    def serialize(self, filename):
        """serialize

        Args:
            data (undefined): data to serialize
            filename (str): file to create
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(self, filename):
        """deserialize

        Args:
            filename (str): file to deserialize
        """
        try:
            with open(filename, "rb") as f:
                loaded_data = pickle.load(f)
        except FileNotFoundError:
            loaded_data = None
        return loaded_data
