#!/usr/bin/python3

bill = float(input("Enter the total: "))

tip1 = bill * .15
# I wasn't able to round the tip in its initial declaration
tip = round(tip1, 2)

total = bill + tip

print ("A 15% tip on",bill,"would be", tip,"The total would be",total)
