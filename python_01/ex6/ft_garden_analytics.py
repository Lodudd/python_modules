#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._show_call = 0
            self._age_call = 0
            self._grow_call = 0

        def increase_show(self) -> None:
            self._show_call += 1

        def increase_age(self) -> None:
            self._age_call += 1

        def increase_grow(self) -> None:
            self._grow_call += 1

        def show_stats(self) -> None:
            print(f"Stats: {self._grow_call} grow,"
                  f"{self._age_call} age, {self._show_call} show")

    def __init__(self, name: str, height: float,
                 myage: int, growth: float) -> None:
        self.statistic = self.Stats()
        self.name = name
        self._height = float(0)
        self.set_height(height)
        self._age = 0
        self.set_age(myage)
        self.growth = growth

    def set_height(self, height: float) -> None:
        if height < 0:
            print("Plant can not be negative!")
        else:
            self._height = height

    def set_age(self, myage: int) -> None:
        if myage < 0:
            print("Age can not be negative")
        else:
            self._age = myage

    def show(self) -> None:
        self.statistic.increase_show()
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self, times: int) -> None:
        self.statistic.increase_grow()
        for days in range(times):
            new_value = round(self._height * self.growth, 2)
            self.set_height(new_value)

    def age(self, times: int) -> None:
        self.statistic.increase_age()
        for days in range(times):
            self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    @staticmethod
    def check_year_old(value: int) -> None:
        if value > 365:
            true_false = True
        else:
            true_false = False
        print(f"Is {value} days more than a year? -> {true_false}")

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        new_plant = cls("Mystery", 0, 0, 0)
        return new_plant


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 myage: int, growth: float, color: str) -> None:
        super().__init__(name, height, myage, growth)
        self.color = color
        self.bloomed = 0

    def show(self) -> None:
        super().show()
        if self.bloomed == 0:
            bloom_info = f"{self.name} has not bloomed yet"
        else:
            bloom_info = f"{self.name} is blooming beautifully!"
        print(f"Color: {self.color}\n{bloom_info}")

    def bloom(self) -> None:
        print(f"Asking {self.name} to bloom")
        self.bloomed = 1


class Tree(Plant):
    statistic: 'TreeStats'

    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.produce_shade_call = 0

        def increase_shade(self) -> None:
            self.produce_shade_call += 1

        def show_stats(self) -> None:
            super().show_stats()
            print(f"{self.produce_shade_call} shades")

    def __init__(self, name: str, height: float,
                 myage: int, growth: float, diameter: int):
        super().__init__(name, height, myage, growth)
        self.trunk_diameter = diameter
        self.statistic = self.TreeStats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> str:
        self.statistic.increase_shade()
        return (f"Tree {self.name} now produces a shade of {self._height:.1f}"
                f"cm long and {self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 myage: int, growth: float, harvest: str):
        super().__init__(name, height, myage, growth)
        self.harvest_season = harvest
        self.nutritional_value = 0.0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}\n"
              f"Nutritional value: {self.nutritional_value}")

    def age(self, times: int) -> None:
        super().age(times)
        self.nutritional_value += 0.5

    def grow(self, times: int) -> None:
        super().grow(times)
        self.nutritional_value += 0.5


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 myage: int, growth: float, color: str):
        super().__init__(name, height, myage, growth, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        if self.bloomed != 0:
            self.seeds = 42
        print(f"Seeds: {self.seeds}")


def Display(Plant: 'Plant') -> None:
    print(f"[Statistic for {Plant.name}]")
    Plant.statistic.show_stats()


if __name__ == "__main__":
    print("=== Check year-old")
    Plant.check_year_old(30)
    Plant.check_year_old(400)

    print("\n====Flower====")
    p1 = Flower("Rose", 15, 1, 1.01, "red")
    p1.show()
    Display(p1)
    p1.bloom()
    p1.grow(10)
    p1.show()
    Display(p1)

    print("\n====Tree====")
    p2 = Tree("Oak", 200, 10, 1.01, 5)
    p2.show()
    Display(p2)
    print(p2.produce_shade())
    Display(p2)

    print("\n====Seed====")
    p3 = Seed("Sunflower", 80, 45, 1.03, "Yellow and Black")
    p3.show()
    p3.bloom()
    p3.age(20)
    p3.grow(20)
    p3.show()
    Display(p3)

    print("\n====Anonymous====")
    p4 = Plant.create_anonymous()
    p4.show()
    Display(p4)
