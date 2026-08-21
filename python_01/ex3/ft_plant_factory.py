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