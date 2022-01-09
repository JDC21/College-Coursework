#!/usr/bin/python3

class Vehicle():
	def __init__(self):
		self.wheels = 4
		self.doors = 4
		self.fuel = 0
		self.temperature = 75
	def get_wheels(self):
		return self.wheels
	def get_doors(self):
		return self.doors
	def get_fuel(self):
		return self.fuel
	def get_temperature(self):
		return self.temperature
	def set_fuel(self,fuel):
		self.fuel = fuel

car = Vehicle()

print(car.get_wheels())
car.set_fuel(100)
