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
