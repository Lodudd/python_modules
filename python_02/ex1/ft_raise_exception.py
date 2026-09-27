#!/usr/bin/env python3
class TempError(Exception):
    def __init__(self, message: str, value: int) -> None:
        super().__init__(message)
        self.message = message
        self.value = value

    def __str__(self) -> str:
        return (f"Caught input_temperature error: {self.value}°C"
                f"is too {self.message} for plants (max 40°C)")


def input_temperature(temp_str: str) -> int:
    print(f"Imput Data Is : '{temp_str}'")
    temperature = int(temp_str)
    if temperature > 40:
        raise TempError("hot", temperature)
    elif temperature < 0:
        raise TempError("cold", temperature)
    return temperature


def test_temperature(temp: str) -> None:
    try:
        x = input_temperature(temp)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    except TempError as e:
        print(e)
    except Exception:
        print("Something mysterious happend !!!")
    else:
        print(f"Temperature is now: {x}°C")


def main() -> None:
    print("=== Garden temperature ===\n")
    test_temperature('25')
    print("\n")
    test_temperature('abc')
    print("\n")
    test_temperature('100')
    print("\n")
    test_temperature('-50')
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
