#!/usr/bin/python3

winning_lotto = "29, 84, 08, 52, 89"
# Without this line the code will match any single number like 2 or 4, so long as it is within the string
winning_lotto = winning_lotto.split(', ')

number = input("enter a number: ")

if number in winning_lotto:
	print(number,"is a winning number!")
else:
	print(number,"is not a winning number")
