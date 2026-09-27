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
        file_name = input("\nEnter new file name (or empty): ")
        if not file_name:
            print("Not saving data.")
        else:
            f1 = open(file_name, 'w')
            print(f"Saving data to'{file_name}'")
            for line in lista:
                f1.write(line + "\n")

    except OSError as e:
        print(f"Error opening file'{sys.argv[1]}': {e}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
