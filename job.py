class Job():

	def __init__(self, hours, family):
		if hours[1] <= hours[0]:
			raise ValueError("Illegal job hours")
		self.hours = hours
		self.family = family