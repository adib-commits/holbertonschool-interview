#!/usr/bin/python3
"""
Module that defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.

    Args:
        n (int): Number of rows

    Returns:
        list: Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        list = [1]

        prev_list = triangle[i - 1]

        for j in range(1, i):
            list.append(prev_list[j - 1] + prev_list[j])

        list.append(1)
        triangle.append(list)

    return triangle
