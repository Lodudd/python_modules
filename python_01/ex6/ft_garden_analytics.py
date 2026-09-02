#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self):
            self._show_call = 0
            self._age_call = 0
            self._grow_call = 0

        def increase_show(self):
            self._show_call += 1

        def increase_age(self):
            self._age_call += 1
        
        def increase_grow(self):
            self._grow_call += 1

        def show_stats(self):
            print(f"Stats: {self._grow_call} grow, {self._age_call} age, {self._show_call} show")

    def __init__(self,name: str,height: float,age: int,growth: float) -> None:
        self.statistic = self.Stats()
        self.name = name
        self._height = float(0)
        self.set_height(height)
        self._age = 0
        self.set_age(age)
        self.growth = growth



    def set_height(self, height: float) -> None:
        if height < 0:
            print("Plant can not be negative!")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        self.statistic.increase_age()
        if age < 0:
            print("Age can not be negative")
        else:
            self._age = age

    def show(self):
        self.statistic.increase_show()
        return f"{self.name}: {self._height}cm, {self._age} days old"

    def grow(self):
        self.statistic.increase_grow()
        new_value = round(self._height * self.growth, 2)
        self.set_height(new_value)

    def aged(self):
        self._age += 1

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    @staticmethod
    def check_year_old(value):
        if value > 365:
            true_false = True
        else:
            true_false = False
        return (f"Is {value} days more than a year? -> {true_false}")

    @classmethod
    def create_anonymous(cls):
        new_plant = cls("Mystery", 0, 0, 0)
        return new_plant


class Flower(Plant):
    def __init__(self, name, height, age, growth, color):
        super().__init__(name, height, age, growth)
        self.color = color
        self.bloomed = 0

    def show(self):
        base_info = super().show()
        extra_info = f"Color: {self.color}"
        if self.bloomed == 0:
            bloom_info = f"{self.name} has not bloomed yet"
        else:
            bloom_info = f"{self.name} is blooming beautifully!"
        return f"{base_info}\n{extra_info}\n{bloom_info}"

    def bloom(self):
        print(f"Asking {self.name} to bloom")
        self.bloomed = 1



class Tree(Plant):
    def __init__(self, name, height, age, growth, diameter):
        super().__init__(name, height, age, growth)
        self.trunk_diameter = diameter

    def show(self):
        base_info = super().show()
        extra_info = f"Trunk diameter: {self.trunk_diameter:.1f}cm"
        return f"{base_info}\n{extra_info}"

    def produce_shade(self):
        return f"Tree {self.name} now produces a shade of {self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."


class Vegetable(Plant):
    def __init__(self, name, height, age, growth, harvest):
        super().__init__(name, height, age, growth)
        self.harvest_season = harvest
        self.nutritional_value = 0

    def show(self):
        base_info = super().show()
        extra_info = f"Harvest season: {self.harvest_season}\nNutritional value: {self.nutritional_value}"
        return f"{base_info}\n{extra_info}"

    def aged(self):
        super().aged()
        self.nutritional_value += 0.5

    def grow(self):
        super().grow()
        self.nutritional_value += 0.5


class Seed(Flower):
    def __init__(self, name, height, age, growth, color):
        super().__init__(name, height, age, growth, color)
        self.seeds = 0

    def show(self):
        base_info = super().show()
        if self.bloomed != 0:
            self.seeds = 42
        bloom_info = f"Seeds: {self.seeds}"
        return f"{base_info}\n{bloom_info}"

def Display(Plant):
    print(f"[Statistic for {Plant.name}]")
    Plant.statistic.show_stats()
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
    for days in range(10):
        p3.aged()
        p3.grow()
    print(p3.show())

    print("=== Check year-old")
    print(Plant.check_year_old(p3.get_age()))
    p3.set_age(400)
    print(Plant.check_year_old(p3.get_age()))
    p4 = Plant.create_anonymous()
    print(p4.show())

    sunflower = Seed("Sunflower", 20, 10, 1.03, "Yellow and Black")
    print(sunflower.show())
    sunflower.bloom()
    print(sunflower.show())

