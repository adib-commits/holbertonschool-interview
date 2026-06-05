#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys


def print_stats(total_size, status_codes):
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))

    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    line_count = 0

    valid_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    try:
        for line in sys.stdin:
            line_count += 1

            try:
                parts = line.split()

                status_code = int(parts[-2])
                file_size = int(parts[-1])

                total_size += file_size

                if status_code in valid_codes:
                    valid_codes[status_code] += 1

            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                print_stats(total_size, valid_codes)

    except KeyboardInterrupt:
        pass

    finally:
        print_stats(total_size, valid_codes)
