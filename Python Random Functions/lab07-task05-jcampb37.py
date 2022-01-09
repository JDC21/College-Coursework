#!/usr/bin/python3

newscales = int(input("Enter scales: "))

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

class ChinesePangolin():
	face = "pointy"
	size = "large"
	scales = 900

	def __init__(tail_length, status, weight_lbs, face, size):
		if size != large:
			return False
		else:
			return size

	def new(newscales):
		if ChinesePangolin.scales + newscales < 1000:
			ChinesePangolin.scales += newscales
			return ChinesePangolin.scales
		else:
			print("Thats a scaly pangolin")
			return False

print(ChinesePangolin.new(newscales))
