#!/usr/bin/python3
# I needed the random module
import random

sides = int(input("Number of sides: "))
roll = random.randint(1,sides)

print ("You rolled a ", roll)
