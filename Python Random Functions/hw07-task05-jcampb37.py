#!/usr/bin/python3
import random

class Coin():
	coin_sides = [1, 2]

	def roll(self):
		return random.choice(self.coin_sides)

	def flip(self):
		out = self.roll()
		if out == 1:
			return "Heads"
		else:
			return "Tails"

	def roll_multiple(self):
		list_of_rolls = []
		for i in range(4):
			list_of_rolls.append(self.roll())
		return list_of_rolls

nickle = Coin()
print(nickle.roll())
print(nickle.flip())
print(nickle.roll_multiple())
