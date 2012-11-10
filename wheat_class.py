from crop_class import *

class Wheat(Crop):
	"""A wheat crop"""

	#constructor
	def __init__(self):
		#call the parent class constructor with default values for Wheat
		#growth rate = 2; light need = 5, water need = 4
		super().__init__(2,5,4)
		self._type = "Wheat" #override the parent class attribute with new value


def main():
	#create a new wheat crop
	wheat_crop = Wheat()
	print(wheat_crop.report())
	#manually grow the crop
	manual_grow(wheat_crop)
	print(wheat_crop.report())
	auto_grow(wheat_crop,15)
	print(wheat_crop.report())

if __name__ == '__main__':
	main()
