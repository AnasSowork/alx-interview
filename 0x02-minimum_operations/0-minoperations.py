#!/usr/bin/python3
"""
Calculates the minimum number of operations needed
to achieve exactly n 'H' characters
using only 'Copy All' and 'Paste' operations.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations required.

    Args:
    - n: Integer, the target number of 'H' characters to achieve.

    Returns:
    - Integer, the minimum number of operations required
    to achieve exactly n 'H' characters.
      Returns 0 if n <= 1.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

# Main file for testing


if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
