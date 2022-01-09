#!/usr/bin/python3

number = float(input("Enter a number: "))

if number < 14.85:
	less = round(14.85 - number, 2)
	print("This is not enough by", less)

if number == 14.85:
	print("That is exactly enough")

if number > 14.85:
	more = round(number - 14.85, 2)
	print("There is change due of", more)
