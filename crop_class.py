class Crop:
	"""A generic food crop"""

	#constructor
	def __init__(self,growth_rate,light_need,water_need):
		#set the attributes with an initial value

		self._growth       = 0
		self._days_growing = 0
		self._growth_rate  = growth_rate
		self._light_need   = light_need
		self._water_need   = water_need
		self._status       = "Seed"
		self._type         = "Generic"

		#the above attributes are prefixed with an underscore to indicate that they should not be
		#accessed directly from outwith the class

	#method to indicate the needs of the crop
	def needs(self):
		#return a dictionary containing the light and water needs
		return {'light need':self._light_need,'water need':self._water_need}

	#method to report the provide information about the current state of the crop
	def report(self):
		#return a dictionary containing type,status,growth and days growing
		return {'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}

	#the underscore indicates that this method should not be called from outwith the class
	def _update_status(self):
		if self._growth > 15:
			self._status = "Old"
		elif self._growth > 10:
			self._status = "Mature"
		elif self._growth > 5:
			self._status = "Young"
		elif self._growth > 0:
			self._status = "Seedling"
		elif self._growth == 0:
			self._status = "Seed"

	def grow(self,light,water):
		if light >= self._light_need and water >= self._water_need:
			self._growth += self._growth_rate
		#increment days growing
		self._days_growing += 1
		#update the status
		self._update_status()

def main():
	#instaniate the class
	new_crop = Crop(1,4,3)
	#test to see whether it works or not
	print(new_crop.needs())
	print(new_crop.report())
	print(new_crop.grow(4,4))
	print(new_crop.report())

if __name__ == '__main__':
	main()