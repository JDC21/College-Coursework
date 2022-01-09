#!/usr/bin/python3

test = input()
test = test.split(", ")

animals = ['dog', 'cat', 'bear', 'fossa', 'tapir']

greetings = []

for t in test:
	if t in animals:
# I found appending 'greetings' before the list had it sucessfully loop through all the correct inputs
		greetings = greetings + ["hello, " + t + "!"]
print(greetings)
