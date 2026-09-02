#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 myage: int, growth: float) -> None:
        self.name = name
        self.height = height
        self.my_age = myage
        self.growth = growth

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.my_age} days old"

    def grow(self) -> None:
        self.height = round(self.height * self.growth, 2)

    def age(self) -> None:
        self.my_age += 1


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30, 1.01)
    weakly_growth = p1.height
    print("=== Garden Plant Growth ===")
    print(p1.show())
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        p1.grow()
        p1.age()
        print(p1.show())
    print(f"Growth this week: {round(p1.height - weakly_growth, 2)}cm")
