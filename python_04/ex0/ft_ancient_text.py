#!/usr/bin/env python3

import sys


def main() -> None:
    try:
        if len(sys.argv) != 2:
            raise Exception(f"Usage: {sys.argv[0]} <file>")

        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        f = open(sys.argv[1])
        print(f.read())
        f.close()
        print(f"File '{sys.argv[1]}' closed.")

    except OSError as e:
        print(f"Error opening file'{sys.argv[1]}': {e}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
