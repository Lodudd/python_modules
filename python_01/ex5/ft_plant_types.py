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


class Flower(Plant):
    def __init__(self, name: str, height: float, myage: int,
                 growth: float, color: str) -> None:
        super().__init__(name, height, myage, growth)
        self.color = color
        self.bloomed = 0

    def show(self) -> str:
        base_info = super().show()
        extra_info = f"Color: {self.color}"
        if self.bloomed == 0:
            bloom_info = f"{self.name} has not bloomed yet"
        else:
            bloom_info = f"{self.name} is blooming beautifully!"
        return f"{base_info}\n{extra_info}\n{bloom_info}"

    def bloom(self) -> None:
        print(f"Asking {self.name} to bloom")
        self.bloomed = 1


class Tree(Plant):
    def __init__(self, name: str, height: float, myage: int,
                 growth: float, diameter: int) -> None:
        super().__init__(name, height, myage, growth)
        self.trunk_diameter = diameter

    def show(self) -> str:
        base_info = super().show()
        extra_info = f"Trunk diameter: {self.trunk_diameter:.1f}cm"
        return f"{base_info}\n{extra_info}"

    def produce_shade(self) -> str:
        return (f"Tree {self.name} now produces a shade of {self._height:.1f}"
                f"cm long and {self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, myage: int,
                 growth: float, harvest: str) -> None:
        super().__init__(name, height, myage, growth)
        self.harvest_season = harvest
        self.nutritional_value = 0.0

    def show(self) -> str:
        base_info = super().show()
        extra_info = (f"Harvest season: {self.harvest_season}\n"
                      f"Nutritional value: {self.nutritional_value}")
        return f"{base_info}\n{extra_info}"

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5


if __name__ == "__main__":
    print("====Flower====")
    p1 = Flower("Rose", 1, 1, 1.01, "red")
    print(p1.show())
    p1.bloom()
    print(p1.show())

    print("====Tree====")
    p2 = Tree("Oak", 200, 10, 1.01, 5)
    print(p2.show())
    print(p2.produce_shade())

    print("====Vegetable====")
    p3 = Vegetable("Tomato", 8, 10, 1.01, "April")
    print(p3.show())
    for days in range(20):
        p3.age()
        p3.grow()
    print(p3.show())
