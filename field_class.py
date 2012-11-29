from potato_class import *
from wheat_class import *
from cow_class import *
from sheep_class import *

class Field:
	"""Simulate a field that can contain animals and crops"""

	#constructor
	def __init__(self,max_crops,max_animals):
		self._crops = []
		self._animals = []
		self._max_animals = max_animals
		self._max_crops = max_crops

	def plant_crop(self,crop):
		if len(self._crops) < self._max_crops:
			self._crops.append(crop)
			return True
		else:
			return False

	def add_animal(self,animal):
		if len(self._animals) < self._max_animals:
			self._animals.append(animal)
			return True
		else:
			return False

	def harvest_crop(self,position):
		return self._crops.pop(position)

	def remove_animal(self,position):
		return self._animals.pop(position)

def display_crops(crop_list):
	print()
	print("The following crops are in this field:")
	for pos in range(len(crop_list)):
		print("{0:>4}. {1}.".format(pos+1,crop_list[pos].report()))

def display_animals(animal_list):
	print("The following animals are in this field:")
	for pos in range(len(animal_list)):
		print("{0:>4}. {1}.".format(pos+1,animal_list[pos].report()))



def main():
	#testing
	new_field = Field(2,5)
	new_field.plant_crop(Wheat())
	new_field.plant_crop(Potato())
	new_field.add_animal(Sheep("Shaun"))
	display_crops(new_field._crops)
	display_animals(new_field._animals)

if __name__ == '__main__':
	main()

	