class Job():

	def __init__(self, hours, family):
		self.check_hours_validity(hours[0], hours[1])
		self.hours = hours
		self.family = family

	def check_hours_validity(self, start, stop):
		if stop <= start:
			raise ValueError("Illegal job hours")

	def calculate_pay(self):
		return 10