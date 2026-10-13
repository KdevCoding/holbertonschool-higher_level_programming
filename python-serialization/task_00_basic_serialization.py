#!/usr/bin/env python3
"""Serialization
"""
import pickle


def serialize_and_save_to_file(data, filename):
    """serialize

    Args:
        data (undefined): data to serialize
        filename (str): file to create
    """

    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """deserialize

    Args:
        filename (str): file to deserialize
    """
    with open(filename, "rb") as f:
        loaded_data = pickle.load(f)
    return loaded_data
