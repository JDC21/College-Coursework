#!/usr/bin/python3

line_grades = [94, 55, 88]

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
	if 76 <= g <= 79:
		grade = 'C+'
	if 70 <= g <= 75:
		grade = 'C'
	if 60 <= g <= 69:
		grade = 'D'
	if g < 60:
		grade = 'E'
	print(grade)
