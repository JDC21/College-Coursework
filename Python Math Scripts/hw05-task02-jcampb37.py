#!/usr/bin/python3
import math

diameter =float( input("Enter the diameter: "))

def area_fun():
#Simply using the integer 3.15 is insufficient I found
	area = math.pi * ((diameter/2)**2)
	print (round(area, 2))

area_fun()
