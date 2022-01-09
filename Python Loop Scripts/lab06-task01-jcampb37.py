#!/usr/bin/python3

hw = input("Enter your hw scores: ")
lab = input("Enter your lab scores: ")

hw = hw.split(', ')
lab = lab.split(', ')

# The code kept failing due to the input being a string, there is no way to turn the input into an int when it is initially declared
hw = [int(h) for h in hw]
lab = [int(l) for l in lab]

sum_hw = sum(hw)
sum_lab = sum(lab)

total = sum_hw + sum_lab

# 900 is exactly 90% of 1000
if total < 900:
	ec = 900 - total
	print("You need at least", ec, "points of extra credit to get a 90% in the class.")
else:
	print("Good job!")
