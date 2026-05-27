#!/usr/bin/python3
"""
Module that calculates the minimum number
of operations needed to obtain n H characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters.

    Args:
        n (int): target number of H characters

    Returns:
        int: minimum number of operations
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

    return operations
