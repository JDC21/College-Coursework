#!/usr/bin/python3
import random

while True:

	sides = (input("Number of sides (quit to stop): "))

	if sides == 'quit':
                exit()

	sides = int(sides)
	roll = random.randint(1,sides)

	print ("You rolled a", roll)
