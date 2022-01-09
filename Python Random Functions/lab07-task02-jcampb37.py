#!/usr/bin/python3

newlength = input("Enter new tail length: ")
number = input("Enter conservation status: ")

class Pangolin():
	tail_length = "long"
	status = "endangered"
	weight_lbs = 5
	def __init__(tail_length, status, weight_lbs):
		tail_length = tail_length
		status = status
		weight_lbs = 5

	def set_tail_length(newlength):
		tail_length = newlength
		return tail_length
	def conservation_status(number):
		if Pangolin.status == number:
			return Pangolin.status
		else:
			return False
print(Pangolin.set_tail_length(newlength))
print(Pangolin.conservation_status(number))
