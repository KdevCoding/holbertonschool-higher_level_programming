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


if __name__ == "__main__":
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
        }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # Output: The data has been serialized and saved to 'data.json'
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)
