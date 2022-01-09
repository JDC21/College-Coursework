#!/usr/bin/python3
import string
import random
from random import *

def pswd():
	source = string.ascii_letters + string.digits
	password =  "".join(choice(source) for c in range(10))
	contains_digit = any(map(str.isdigit, password))
	if contains_digit == True:
		print (password)
	else:
		pswd()
pswd()
