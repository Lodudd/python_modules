#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Imput Data Is : '{temp_str}'")
    temperature = int(temp_str)
    return temperature


def test_temperature(temp: str) -> None:
    try:
        x = input_temperature(temp)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    except Exception:
        print("Something else")
    else:
        print(f"Temperature is now: {x}°C")


def main() -> None:
    print("=== Garden temperature ===\n")
    test_temperature('25')
    print("\n")
    test_temperature('abc')
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
