#!/usr/bin/python3
import math

p1 = (input("Enter the first point: "))
#In order to accept input in (x, y) format, I needed to replace the parentheses with whitespaces
p1 = p1.replace('(', ' ')
p1 = p1.replace(')', ' ')
#I then split apart the integers based on a comma
p1= p1.split (',')
x1 = float(p1[0])
y1 = float(p1[1])

p2 = (input("Enter the second point: "))
p2 = p2.replace('(', ' ')
p2 = p2.replace(')', ' ')
p2= p2.split (',')
x2 = float(p2[0])
y2 = float(p2[1])

#I decided to use a simple function, the math itself was the easy part
def distance_point():
        sum = (((x2-x1)**2)+((y2-y1)**2))**0.5
        print (round(sum, 1))

distance_point()
