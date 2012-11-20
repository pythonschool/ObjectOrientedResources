class Animal:
	"""a generic animal"""

	#constructor
	def __init__(self,growth_rate,food_need,water_need):
		#set the attributes with an initial value

		self._weight = 0
		self._days_growing = 0
		self._growth_rate = growth_rate
		self._food_need = food_need
		self._water_need = water_need
		self._status = "Baby"
		self._type = "Generic"

		#the above attributes are prefixed with an underscore to indicate that they should not be
		#accessed directly from outwith the class

	#method to indicate the needs of the animal
	def needs(self):
		#return a dictionary containing the food and water needs
		return {'food need':self._food_need,'water need':self._water_need}

	#method to provide information about the current state of the animal
	def report(self):
		#return a dictionary containing type,status, weight and days growing
		return {'type':self._type,'status':self._status,'weight':self._weight,'days growing':self._days_growing}