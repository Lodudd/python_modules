#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 myage: int, growth: float) -> None:
        self.name = name
        self._height = 0.0
        self.set_height(height)
        self._age = 0
        self.set_age(myage)
        self.growth = growth

    def set_height(self, height: float) -> None:
        if height < 0:
            print(self.name + ": Error, height can't be negative!")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, myage: int) -> None:
        if myage < 0:
            print(f"{self.name}: Error, age can not be negative")
            print("Age update rejected")
        else:
            self._age = myage

    def show(self) -> str:
        return f"{self.name}: {self._height}cm, {self._age} days old"

    def grow(self) -> None:
        new_value = round(self._height * self.growth, 2)
        self.set_height(new_value)

    def age(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def __str__(self) -> str:
        return self.show()


if __name__ == "__main__":

    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15, 10, 1.01)
    print(f"Plant Created: {p1} \n")
    p1.set_height(25)
    print("Height updated: " + str(p1.get_height()) + "cm")
    p1.set_age(30)
    print(f"Age updated: {p1.get_age()} days")
    print("\n")
    p1.set_height(-10)
    p1.set_age(-10)
    print("\n")
    print("Current state: " + p1.show())
