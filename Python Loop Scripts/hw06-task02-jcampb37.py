#!/user/bin/python3

Faculty = ["Rucker", "Gatto", "Doheny", "Ingersoll", "Lauer"]
Students = ["Johnson", "Russell", "Zeck", "Nehdar", "Sainz"]

name = input("Enter a name: ")

if name in Faculty:
	print ("Welcome, Professor",name,"!")
if name in Students:
	print ("Hello, Sutdent! The next assignment is Homework 6.")
