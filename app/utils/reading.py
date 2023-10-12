"""
reading.py

This file contains all of our reading methods
"""

import io

def read_file_as_bytes(file_path: str) -> io.BytesIO:
    """
    Reads a file and returns its contents as bytes.

    :param file_path: The path to the file to read.
    :return: A BytesIO object containing the file bytes.
    """
    with open(file_path, "rb") as file:
        file_bytes = file.read()
        bytes_io = io.BytesIO(file_bytes)
        return bytes_io