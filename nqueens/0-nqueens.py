#!/usr/bin/python3
"""N Queens problem solver"""

import sys


def is_safe(queens, row, col):
    """Check if position is safe"""
    for queen in queens:
        if queen[1] == col:
            return False

        if abs(queen[0] - row) == abs(queen[1] - col):
            return False

    return True


def solve(n, row, queens):
    """Solve N Queens with backtracking"""
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve(n, row + 1, queens)
            queens.pop()


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(n, 0, [])


if __name__ == "__main__":
    main()
