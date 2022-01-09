#!/usr/bin/python3

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
	def __str__():
		return weight_lbs

	def __len__():
		return tail_length

	def __eq__(other):
		if Pangolin.status == other:
			return True
		else:
			return False
		print(Pangolin.__eq__(other))

class SafePangolin(Pangolin):
	def new_status(number):
		if status != "endangered":
			status = safe
			return status
		else:
			return False

	def arboreal():
		weight_lbs = 3
		return weight_lbs
