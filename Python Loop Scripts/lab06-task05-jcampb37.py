#!/usr/bin/python3
import csv

first = input()
yes = 0

with open("./addresses.csv", "r") as csv_file:
	lines = csv.reader(csv_file)

	for l in lines:
		l = l[0]
		name = l.split(': ')[0]
		address = l.split(': ')[1]
		if first == name:
			print("{}: {}" .format(first, address))
			yes += 1
			exit()
if yes == 0:
	new = input("Add address: ")
	new_add = ("{}: {}" .format(first, new))

with open("./addresses.csv", "a") as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([new_add])
