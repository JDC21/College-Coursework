#!/usr/bin/python3

names = input()
numbers = (input())
#The split will change each string into a list
names = names.split(", ")
numbers = numbers.split(", ")

Grades = {}

for i in range(len(names)):
	Grades[names[i]]=numbers[i]

print (Grades)
