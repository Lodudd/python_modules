#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')
    if operation_number == 1:
        42/0
    if operation_number == 2:
        open("notexist.txt", "r")
    if operation_number == 3:
        "one" + 3
    return


def test_error_types(number: int) -> None:
    try:
        print(f"Testing operation {number}...")
        garden_operations(number)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    except Exception:
        print("Mystery error!!!")
    else:
        print("Operation completed successfully")


def main() -> None:
    print("=== Garden Error Types Demo ===\n")
    for i in range(5):
        test_error_types(i)
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
