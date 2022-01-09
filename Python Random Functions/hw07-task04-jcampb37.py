#!/usr/bin/python3
from random import randint

# Many similarities between this code and task 5
class Die():

	def __init__(self, sides):
		self.sides = sides

	def roll(self):
		return randint(1, self.sides)

	def roll_multiple(self):
		list_of_rolls = []
		for i in range(4):
			list_of_rolls.append(self.roll())
		return list_of_rolls

	def get_sides(self):
		return self.sides

idie = Die(20)
print(idie.get_sides())
print(idie.roll())
print(idie.roll_multiple())
