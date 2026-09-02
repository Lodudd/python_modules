#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float,
                 myage: int, growth: float) -> None:
        self.name = name
        self.height = height
        self.myage = myage
        self.growth = growth

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.myage} days old"

    def grow(self) -> None:
        self.height = round(self.height * self.growth, 2)

    def age(self) -> None:
        self.myage += 1


if __name__ == "__main__":
    plants = [
        Plant("Rose", 15, 20, 1.01),
        Plant("Tulip", 8, 5, 1.03),
        Plant("Cactus", 30, 100, 1.001),
        Plant("Sunflower", 45, 15, 1.05),
        Plant("Fern", 12, 40, 1.02),
    ]
    print("=== Plant Factory Output ===")
    for i in plants:
        print("Created:", i.show())
