#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of a string object.
    Args:
        my_obj (str): The object to serialize.
    Returns:
        The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
