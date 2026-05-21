#!/usr/bin/python3
"""
Module that determines if all lockboxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): A list of lists containing keys.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """

    opened = set([0])
    keys = [0]

    while keys:
        current = keys.pop()

        for key in boxes[current]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                keys.append(key)

    return len(opened) == len(boxes)
