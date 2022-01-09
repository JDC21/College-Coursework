#!/usr/bin/python3

string1 = "Shaun, Sammy, Brandon, Arielle, Erik, Steven"
#This line will get rid of the preceding space of all items
string1 = string1.replace(" ", "")
string1 = string1.split(',')
string2 = "89, 97, 47, 99, 69, 94"
string2 = string2.replace(" ", "")
string2 = string2.split(',')
name = int(input("Enter an entry: "))
grade = int(input("Enter an entry: "))

#I needed to seperate the outputs, otherwise there would be a space between the name and the ';'
print (string1[name], end = '')
print (":", string2[grade])
