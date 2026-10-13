#!/usr/bin/env python3
"""Serialization
"""
import csv
import json


def convert_csv_to_json(filename):
    """convert csv to json

    Args:
        filename (str):
    """
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))
    except FileNotFoundError:
        return False

    with open('output.json', mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile)
    return True


if __name__ == "__main__":
    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")
