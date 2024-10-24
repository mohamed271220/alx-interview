#!/usr/bin/python3
"""
Log parsing script
"""
import sys


def print_stats(file_size, status_counts):
    """
    Print the statistics of file size and status counts
    """
    print("File size: {}".format(file_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))


def main():
    """
    Main function to parse logs and compute metrics
    """
    file_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) > 6:
                try:
                    file_size += int(parts[-1])
                    status_code = int(parts[-2])
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                except (ValueError, IndexError):
                    pass

            if line_count % 10 == 0:
                print_stats(file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_counts)
        raise

    print_stats(file_size, status_counts)


if __name__ == "__main__":
    main()
