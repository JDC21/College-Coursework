#!/usr/bin/python3
import math

op = 'xxx'

while True:
	if op == 'quit':
		exit()
	calc = input("Enter calculation (enter quit to stop): ")
	calc = calc.split()
# I seperate the operator into its own variable, rather than calling calc[0] every time
	op = calc[0]
	del calc[0]

	calc = [int(c) for c in calc]

	if op == 'add':
		sum_calc = sum(calc)
		print ("Sum:",sum_calc)

	if op == 'sub':
		diff_calc = calc[0]
		for c in calc[1:]:
			diff_calc = diff_calc - c
		print("Difference:",diff_calc)

	if op == 'mul':
		mul_calc = calc[0]
		for c in calc[1:]:
			mul_calc = mul_calc * c
		print("Product:",mul_calc)

	if op == 'div':
		div_calc = calc[0]
		for c in calc[1:]:
			div_calc = div_calc / c
		print("Qotient:",div_calc)

	if op == 'exp':
		exp_calc = calc[0]
		for c in calc[1:]:
			exp_calc = exp_calc ** c
		print("Power:",exp_calc)

	if op == 'mod':
		mod_calc = calc[0]
		for c in calc[1:]:
			mod_calc = mod_calc % c
		print("Modulus:",mod_calc)
