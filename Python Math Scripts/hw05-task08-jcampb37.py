#!/usr/bin/python3

number = int(input("Enter a number of seconds: "))

def time():
	seconds = number % (24 * 3600)
	hours = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60
# I did not know if we needed to make variable statements for plural 'hours' singular 'minute' or singular 'second'
	print(hours,"hour", minutes,"minutes", seconds,"seconds")

time()
