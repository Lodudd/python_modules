#!/usr/bin/env python3

import sys


def main() -> None:
    inventory: dict[str, int] = {}

    for i in range(1, len(sys.argv)):
        try:
            nieitem = sys.argv[i].split(":")
            if len(nieitem) != 2:
                raise Exception(f"Error - invalid parameter '{sys.argv[i]}'")
            value = int(nieitem[1])
            name = nieitem[0]
            if name not in inventory:
                inventory[name] = value
        except ValueError as e:
            print(f"Quantity error for'key': {e}")
        except Exception as e:
            print(e)

    print(f"Got inventory: {inventory}")
    print(f"Item list:: {list(inventory.keys())}")
    test = sum(inventory.values())
    print(f"Total quantity of {len(inventory)} items: {test}")

    for item, value in inventory.items():
        print(f"Item {item} represents: {value/test:.1%}")

    inventory.update({"magic_item": 1})
    try:
        most = max(inventory.values())
        least = min(inventory.values())
    except ValueError:
        print("not good")

    for item, value in inventory.items():
        if most == value:
            print(f"Item most abundant: {item} with quantity {value}")
            break
    for item, value in inventory.items():
        if least == value:
            print(f"Item least abundant: {item} with quantity {value}")
            break
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
