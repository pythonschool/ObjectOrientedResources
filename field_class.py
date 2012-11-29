from potato_class import *
from wheat_class import *
from animal_class import *

class Field:
	"""Simulate a field that can contain animals and crops"""

	#constructor
	def __init__(self,max_animals,max_crops):
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


def main():
	pass

if __name__ == '__main__':
	main()

	