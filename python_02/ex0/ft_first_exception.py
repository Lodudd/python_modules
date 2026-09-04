#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    return temperature

def test_temperature(temp: str):
    try:
        x = input_temperature(temp)
    except Exception:
        print("provide string")
    else:
        return x
if __name__ == "__main__":
    x = 1 + test_temperature('10')
    print(x)
