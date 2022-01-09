#!/usr/bin/python3

cost = float(input("Cost is "))
payment = (input("Enter a payment: "))
# coins will not be declared above the if statements to conform with the expected output

if payment == 'quit':
        print("Goodbye")
        exit()

# each instance of the payment variable will have to be manually made a floating integer, so that a 'quit' input will read for the first if statement
if float(payment) == cost:
	print ("No change due")

if float(payment) < cost:
	coins = input("Enter a list of coin values: ")
	coins = coins.split(', ')
	less = str( round(cost - float(payment), 2) )
	dollars = less.split('.')[0]
	cents = less.split('.')[1]
	thirty_five = str( int(cents) / (float(coins[1]) * 100) ).split('.')[0]
	twenty_three = str( (int(cents) - (int(thirty_five) * (float(coins[1]) * 100) )) / (float(coins[2]) * 100) ).split('.')[0]
	twelve = str((int(cents) - (int(thirty_five) * (float(coins[1]) * 100) ) - (int(twenty_three) * (float(coins[2]) * 100) )) / (float(coins[3]) * 100) ).split('.')[0]
	three = str((int(cents) - (int(thirty_five) * (float(coins[1]) * 100) ) - (int(twenty_three) * (float(coins[2]) * 100) ) - (int(twelve) * (float(coins[3]) * 100) )) / (float(coins[4]) * 100) ).split('.')[0]
	one = str((int(cents) - (int(thirty_five) * (float(coins[1]) * 100) ) - (int(twenty_three) * (float(coins[2]) * 100) ) - (int(twelve) * (float(coins[3]) * 100) ) - (int(three) * (float(coins[5]) * 100) )) / 1).split('.')[0]
	print ("needed:", dollars, coins[0], "coins,", thirty_five, coins[1], "coins,", twenty_three, coins[2], "coins,", twelve, coins[3], "coins,", three, coins[4], "coins,", one, coins[5], "coins")

if float(payment) > cost:
	coins = input("Enter a list of coin values: ")
	coins = coins.split(', ')
	more = str( round(float(payment) - cost, 2) )
	dollars = more.split('.')[0]
	cents = more.split('.')[1]
	thirty_five = str( int(cents) / (float(coins[1]) * 100) ).split('.')[0]
	twenty_three = str( (int(cents) - (int(thirty_five) * (float(coins[1]) * 100) )) / (float(coins[2]) * 100) ).split('.')[0]
	twelve = str((int(cents) - (int(thirty_five) * (float(coins[1]) * 100) ) - (int(twenty_three) * (float(coins[2]) * 100) )) / (float(coins[3]) * 100) ).split('.')[0]
	three = str((int(cents) - (int(thirty_five) * (float(coins[1]) * 100) ) - (int(twenty_three) * (float(coins[2]) * 100) ) - (int(twelve) * (float(coins[3]) * 100) )) / (float(coins[4]) * 100) ).split('.')[0]
	one = str((int(cents) - (int(thirty_five) * (float(coins[1]) * 100) ) - (int(twenty_three) * (float(coins[2]) * 100) ) - (int(twelve) * (float(coins[3]) * 100) ) - (int(three) * (float(coins[5]) * 100) )) / 1).split('.')[0]
	print ("change:", dollars, coins[0], "coins,", thirty_five, coins[1], "coins,", twenty_three, coins[2], "coins,", twelve, coins[3], "coins,", three, coins[4], "coins,", one, coins[5], "coins")
