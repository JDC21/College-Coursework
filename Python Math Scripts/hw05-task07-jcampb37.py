#!/usr/bin/python3.9

# IMPORTANT: in order to run this code properly, I had to use 'python3.9 ./hw05-task07-jcampb37.py' something to do with the f-string didn't work on my machine, just in case you have the same issue

info = input()
info = info.split(', ')

name = info[0]
occupation = info[1]
birth_month = info[2]
birth_state = info[3]
interests = info[4]
relative = info[5]


print(f"My name is {name}. I was born in {birth_month}. I am a fiercely loyal {occupation}. You might think I’m crazy, but I  was born in {birth_state} so I can't help it. I like {interests}, but I love my {relative}. And yes, they bought me this shirt.")
