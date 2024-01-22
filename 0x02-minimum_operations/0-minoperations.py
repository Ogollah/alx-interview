#!/usr/bin/env python3
"""
A method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters.
    """
    if n <= 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return minOperations(n // i) + i

    return n
