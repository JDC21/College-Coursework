#!/usr/bin/python3
import sys
from io import StringIO

myfile = open("./lab0604.csv", "r")
next(myfile)
lines = myfile.readlines()

line = []
last = [("Name Grade Letter")]

print("Name Grade Letter")
X = 0
for m in lines:
	line.append(m.strip())
	grades = line[X].split(',')[1:]
	grades_int = [int(i) for i in grades]
	name = line[X].split(',')[0]
	line_avg = round(sum(grades_int) / 8, 2)
	line_grades = [line_avg]
	for g in line_grades:
		if 97 <= g <= 100:
			grade = 'A+'
		if 94 <= g <= 96:
			grade = 'A'
		if 90 <= g <= 93:
			grade = 'A-'
		if 87 <= g <= 89:
			grade = 'B+'
		if 84 <= g <= 86:
			grade = 'B'
		if 80 <= g <= 83:
			grade = 'B-'
		if 76 <= g < 80:
			grade = 'C+'
		if 70 <= g <= 75:
			grade = 'C'
		if 60 <= g <= 69:
			grade = 'D'
		if g < 60:
			grade = 'E'
	print(name, line_avg, grade)
	X += 1
	last.append(name + " " + str(line_avg) + " " + grade)
myfile.close

newfile = open("./out604.txt", "w")
for l in last:
	for i in l:
		newfile.write(str(i)+"")
	newfile.write("\n")
	print()
newfile.close
