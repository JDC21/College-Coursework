#!/usr/bin/python3

value = input("Enter a value: ")
coins = input("Enter coins: ")
coins = coins.split(', ')

dollars = value.split('.')[0]
# the following line takes 13.37 and takes '37', we want '.37', in order to remediate that, all 'coins' are multiplied by 100
cents = value.split('.')[1]
thirty_five = str( int(cents) / (float(coins[1]) * 100) ).split('.')[0]
twenty_three = str( (int(cents) - (int(thirty_five) * (float(coins[1]) * 100) )) / (float(coins[2]) * 100) ).split('.')[0]
twelve = str((int(cents) - (int(thirty_five) * (float(coins[1]) * 100) ) - (int(twenty_three) * (float(coins[2]) * 100) )) / (float(coins[3]) * 100) ).split('.')[0]
three = str((int(cents) - (int(thirty_five) * (float(coins[1]) * 100) ) - (int(twenty_three) * (float(coins[2]) * 100) ) - (int(twelve) * (float(coins[3]) * 100) )) / (float(coins[4]) * 100) ).split('.')[0]

value_dict = {coins[0]+' coins': dollars, coins[1]+' coin' : thirty_five, coins[2]+' coin' : twenty_three, coins[3]+' coin' : twelve, coins[4]+' coin' : three}

print(value_dict)

