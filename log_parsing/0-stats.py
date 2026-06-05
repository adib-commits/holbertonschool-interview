#!/usr/bin/python3
"""Log parsing script that reads stdin and computes metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Main function to parse log lines from stdin."""
    total_size = 0
    line_count = 0
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    status_counts = {code: 0 for code in valid_codes}

    try:
        for line in sys.stdin:
            parts = line.split()
            try:
                # Expected format:
                # <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>
                # Minimum parts check
                if len(parts) < 7:
                    continue
                # File size is the last token
                file_size = int(parts[-1])
                # Status code is second to last
                status_code = int(parts[-2])

                # Validate the line structure more carefully
                if parts[1] != '-':
                    continue
                if not parts[2].startswith('['):
                    continue
                if '"GET' not in line or 'HTTP/1.1"' not in line:
                    continue

                total_size += file_size
                if status_code in valid_codes:
                    status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

            except (ValueError, IndexError):
                continue

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
