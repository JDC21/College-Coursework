#!/usr/bin/python3
import math

order = input("Please enter your order: ")

cost = 0

for x in order.split(','):
	if x == '1':
		cost += 7.90
	if x == '2':
		cost += 8.82
	if x == '3':
		cost += 14.53
	if x == '4':
		cost += 9.96
	if x == '5':
		cost += 25.09

cost = str(cost)
dollars = cost.split('.')[0]
cents = cost.split('.')[1]
quarters = str(int(cents) / 25).split('.')[0]
dimes = str((int(cents) - (int(quarters) * 25)) / 10).split('.')[0]
nickels = str((int(cents) - (int(quarters) * 25) - (int(dimes) * 10)) / 5).split('.')[0]
pennies = str((int(cents) - (int(quarters) * 25) - (int(dimes) * 10) - (int(nickels) * 5)) / 1).split('.')[0]

print("Order total: ", cost)
print("Dollars:", dollars)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
