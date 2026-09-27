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

        f = open(sys.argv[1])
        lista = []
        while True:
            new_line = f.readline().replace("\n", "")
            if not new_line:
                break
            lista.append(new_line + "#")
        f.close()
        print("\nEnter new file name (or empty): ", end="")
        file_name = sys.stdin.readline()
        if not file_name:
            print("Not saving data.")
        else:
            f1 = open(file_name, 'w')
            print(f"Saving data to'{file_name[:-1]}'")
            for line in lista:
                f1.write(line + "\n")

    except OSError as e:
        print(f"[STDERR] Error opening file'{sys.argv[1]}': {e}",
              file=sys.stderr)
    except Exception as e:
        print(f"[STDERR] {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
