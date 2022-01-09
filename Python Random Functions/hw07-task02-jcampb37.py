#!/usr/bin/python3

# This code has not expected output, so I did not include any prints
class Dog():
	def __init__(self, name, life_expectancy, size, coat_type, coat_color):
		self.name = name
		self.life_expectancy =life_expectancy
		self.size = size
		self.coat_type = coat_type
		self.coat_color = coat_color
	def get_name(self):
		return self.name
	def get_life(self):
		return self.life_expectancy
	def get_size(self):
		return self.size
	def get_coat_type(self):
		return self.coat_type
	def get_coat_color(self):
		return self.coat_color

gr = Dog("Golden Retriever", 12, "large", "medium", "gold")
pg = Dog("Pug", 15, "small", "short","silver fawn")
cg = Dog("Corgi", 13, "smol", "fluffy", "tricolor")
