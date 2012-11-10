from crop_class import *

class Potato (Crop):
	"""A potato crop"""

	#contructor
	def __init__(self):
		#call the parent class constructor with default values for Potato
		#growth rate = 1; light need = 3, water need = 6
		super().__init__(1,3,6)
		self._type = "Potato"