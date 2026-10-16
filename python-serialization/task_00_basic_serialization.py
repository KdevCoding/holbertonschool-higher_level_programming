#!/usr/bin/python3
"""serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save it to filename

    An existing file is replaced
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and return the deserialized dictionary"""
    with open(filename, "r") as f:
        return json.load(f)
