#!/usr/bin/python3

value = input("Enter a value: ")

dollars = value.split('.')[0]
cents = value.split('.')[1]
thirty_five = str(int(cents) / 35).split('.')[0]
twenty_three = str((int(cents) - (int(thirty_five) * 35)) / 23).split('.')[0]
twelve = str((int(cents) - (int(thirty_five) * 35) - (int(twenty_three) * 23)) / 12).split('.')[0]
three = str((int(cents) - (int(thirty_five) * 35) - (int(twenty_three) * 23) - (int(twelve) * 12)) / 3).split('.')[0]
one = str((int(cents) - (int(thirty_five) * 35) - (int(twenty_three) * 23) - (int(twelve) * 12) - (int(three) * 3)) / 1).split('.')[0]

value_dict = {'1 dollar': dollars, '.35 coin' : thirty_five, '.23 coin' : twenty_three, '.12 coin' : twelve, '.03 coin' : three, '.01 coin' : one}

print(value_dict)
