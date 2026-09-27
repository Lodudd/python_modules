#!/usr/bin/env python3

import sys


def show_args(args: list[str]) -> None:

    arguments = len(args)
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")

    if arguments == 1:
        print("No arguments provided!")
    else:
        print("Arguments received: " + str(arguments - 1))

    for i in range(1, arguments):
        print(f"Argument {i}: {args[i]}")
    print("Total arguments: " + str(arguments))


def main(args: list[str]) -> None:
    show_args(args)


if __name__ == "__main__":
    main(sys.argv)
