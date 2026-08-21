#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

	def show(self):
		return f"{self.name}: {self.height}cm, {self.age} days old"


plants = [
	Plant("Rose", 25, 30),
	Plant("Sunflower", 80, 45),
	Plant("Cactus", 15, 120)
]

print("=== Garden Plant Registry ===")
for i in plants:
	print(i.show())
