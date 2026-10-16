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
    for item in dictionary:
        item_ele = ET.SubElement(root, item)
        item_ele.text = dictionary[item]

    new_tree = ET.ElementTree(root)
    new_tree.write(filename, xml_declaration=True)


def deserialize_from_xml(filename):
    """deserialize

    Args:
        filename (str): file to deserialize
    """
    try:
        tree = ET.parse("data.xml")
        root = tree.getroot()

        flat_dict = {child.tag: child.text for child in root}
    except FileNotFoundError:
        flat_dict = None
    return flat_dict
