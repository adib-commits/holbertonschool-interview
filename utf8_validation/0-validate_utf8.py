#!/usr/bin/python3
"""
UTF-8 validation module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers.

    Returns:
        bool: True if valid UTF-8, otherwise False.
    """
    nb_bytes = 0

    for num in data:
        byte = num & 0xFF

        if nb_bytes == 0:
            mask = 0x80

            while mask & byte:
                nb_bytes += 1
                mask >>= 1

            if nb_bytes == 0:
                continue

            if nb_bytes == 1 or nb_bytes > 4:
                return False

            nb_bytes -= 1
        else:
            if not (byte & 0x80 and not (byte & 0x40)):
                return False

            nb_bytes -= 1

    return nb_bytes == 0
