#!/usr/bin/python3

animals = input()

animals = animals.split(", ")

greetings = [ "hello, " + i + "!" for i in animals]

print(greetings)
