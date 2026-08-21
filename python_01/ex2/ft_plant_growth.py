#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, age, growth):
		self.name = name
		self.height = height
		self.age = age
		self.growth = growth

	def show(self):
		return f"{self.name}: {self.height}cm, {self.age} days old"

	def grow(self):
		self.height = round(self.height * self.growth, 2)
	def aged(self):
		self.age += 1

p1 = Plant("Rose", 25, 30, 1.01)
weakly_growth = p1.height
print("=== Garden Plant Growth ===")
print(p1.show())
for day in range(1,8):
	print(f"=== Day {day} ===")
	p1.grow()
	p1.aged()
	print(p1.show())

print(f"Growth this week: {round(p1.height - weakly_growth, 2)}cm")