#!/usr/bin/python3

class Rectangle():
# without the added arguments below, 'length and width' the code will fail
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def getrect(self):
		return self.length, self.width

	def get_area(self):
		return self.length * self.width

	def is_square(self):
		if self.width == self.length:
			return True
		return False

	def __eq__(self,other):
		if self.length == other.length and self.width == other.width:
			return True
		return False

abrect = Rectangle(10,10)
cdrect = Rectangle(10,10)
shrect = Rectangle(10,15)
print(shrect.getrect())
print(abrect.get_area())
print(cdrect.is_square())
print(shrect == abrect)
print(abrect == cdrect)
