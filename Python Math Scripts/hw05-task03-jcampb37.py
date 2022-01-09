#!/usr/bin/python3

names = input("Enter a string of names ")
#Without this line, the sort will not account for the 'spaces' between words, and will not sort correctly
names = names.replace(" ", "")
#This will change the string into a list, capable of being sorted
names = names.split(',')

names.sort()

print (names)
