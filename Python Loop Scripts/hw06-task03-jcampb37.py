#!/usr/bin/python3

one = input("Enter first list: ")
two = input("Enter second list: ")

one = one.split(", ")
two = two.split(", ")

for o in one:
	for t in two:
		print(o, t)
