#!/usr/bin/python3
"""
This module reads from standard input and computes metrics
"""
import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
size_summation = 0
line_count = 0

def print_logs():
    """
    Prints the computed metrics.
    """
    print("File size: {}".format(size_summation))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            parts = line.strip().split()
            # Ensure the line has the correct format
            if len(parts) < 7:
                continue
            
            try:
                # Extract the file size and status code
                file_size = int(parts[-1])
                status_code = int(parts[-2])

                # Update size and count if valid status code
                size_summation += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

                line_count += 1

                # Print every 10 lines
                if line_count % 10 == 0:
                    print_logs()

            except (ValueError, IndexError):
                continue

        print_logs()

    except KeyboardInterrupt:
        print_logs()
        raise
