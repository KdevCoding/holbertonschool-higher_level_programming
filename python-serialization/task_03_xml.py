#!/usr/bin/env python3
"""Serialization"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize
    Args:
        data (undefined): data to serialize
        filename (str): file to create
    """

    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = "" if value is None else str(value)

    new_tree = ET.ElementTree(root)
    new_tree.write(filename)


def deserialize_from_xml(filename):
    """deserialize

    Args:
        filename (str): file to deserialize
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        flat_dict = {child.tag: child.text for child in root}
    except FileNotFoundError:
        flat_dict = None
    return flat_dict
