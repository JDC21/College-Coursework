#!/usr/bin/python3
import math

length_C = int(input("Enter the length of c: "))
angle_B = int(input("Enter the angle of b: "))
angle_C = 90

def Pythagoras():
# sin and cos in python expects the number to already be in radians, not degrees, so its necessary to add math.radians
	length_B = (round((math.sin(math.radians(angle_B)))*length_C, 2))
	length_A = (round((math.cos(math.radians(angle_B)))*length_C, 2))
	angle_A = 180-angle_C-angle_B
	print("Angle a: ", angle_A)
	print("Length b: ",length_B)
	print("Length a: ", length_A)

Pythagoras()
