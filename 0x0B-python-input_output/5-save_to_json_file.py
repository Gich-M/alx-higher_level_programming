#!/usr/bin/python3
"""
    Defines a function that writes an Object to a text file,
    using a JSON representation.
    """
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to serialize.
        filename (str): The name of the file to write.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
