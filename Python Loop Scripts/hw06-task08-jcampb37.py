#!/usr/bin/python3

value = float(input("Enter a value: "))

if value == 16.48:
  	print("No change due")

if value > 16.48:
	more = str(round(value - 16.48, 2))
	dollars = more.split('.')[0]
	cents = more.split('.')[1]
	thirty_five = str(int(cents) / 35).split('.')[0]
	twenty_three = str((int(cents) - (int(thirty_five) * 35)) / 23).split('.')[0]
	twelve = str((int(cents) - (int(thirty_five) * 35) - (int(twenty_three) * 23)) / 12).split('.')[0]
	three = str((int(cents) - (int(thirty_five) * 35) - (int(twenty_three) * 23) - (int(twelve) * 12)) / 3).split('.')[0]
	one = str((int(cents) - (int(thirty_five) * 35) - (int(twenty_three) * 23) - (int(twelve) * 12) - (int(three) * 3)) / 1).split('.')[0]
	more_dict = {'1 dollar': dollars, '.35 coin' : thirty_five, '.23 coin' : twenty_three, '.12 coin' : twelve, '.03 coin' : three, '.01 coin' : one}
	print("Change: ",dollars,"dollars,",thirty_five,".35 coins,",twenty_three,".23 coins,",twelve,".12 coins,",three,".03 coins,",one,".01 coins")

if value < 16.48:
	less = str(round(16.48 - value, 2))
	dollars = less.split('.')[0]
	cents = less.split('.')[1]
	thirty_five = str(int(cents) / 35).split('.')[0]
	twenty_three = str((int(cents) - (int(thirty_five) * 35)) / 23).split('.')[0]
	twelve = str((int(cents) - (int(thirty_five) * 35) - (int(twenty_three) * 23)) / 12).split('.')[0]
	three = str((int(cents) - (int(thirty_five) * 35) - (int(twenty_three) * 23) - (int(twelve) * 12)) / 3).split('.')[0]
	one = str((int(cents) - (int(thirty_five) * 35) - (int(twenty_three) * 23) - (int(twelve) * 12) - (int(three) * 3)) / 1).split('.')[0]
	less_dict = {'1 dollar': dollars, '.35 coin' : thirty_five, '.23 coin' : twenty_three, '.12 coin' : twelve, '.03 coin' : three, '.01 coin' : one}
	print("Needed: ",dollars,"dollars,",thirty_five,".35 coins,",twenty_three,".23 coins,",twelve,".12 coins,",three,".03 coins,",one,".01 coins")
