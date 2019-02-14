class Job():

	def __init__(self, hours, family):
		self.check_hours_validity(hours[0], hours[1])
		self.hours = hours
		self.family = family

	def check_hours_validity(self, start, stop):
		if stop <= start:
			raise ValueError("Illegal job hours")

	def calculate_pay(self):
		hours_on_job = self.hours[1] - self.hours[0]
		return hours_on_job.total_seconds() / 60 / 60 * self.family.price_by_hour[0][0]