#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, age, growth):
		self.name = name
		self._height = 0
		self.set_height(height)
		self._age = 0
		self.set_age(age)
		self.growth = growth

	def set_height(self, height):
		if height < 0:
			print ("Plant can not be negative!")
		else:
			self._height = height

	def set_age(self, age):
		if age < 0:
			print("Age can not be negative")
		else:
			self._age = age

	def show(self):
		return f"{self.name}: {self._height}cm, {self._age} days old"

	def grow(self):
		self.set_height = round(self._height * self.growth, 2)
	def aged(self):
		self._age += 1
	def get_height(self):
		return self._height
	def get_age(self):
		return self._age

if __name__ == "__main__":

	p1 = Plant("test", 1, 1, 1.01)
	print(p1.get_height())