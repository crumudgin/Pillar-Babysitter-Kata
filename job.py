class Job():

	def __init__(self, hours, family):
		self.check_hours_validity(hours[0], hours[1])
		self.hours = hours
		self.family = family

	def check_hours_validity(self, start, stop):
		if stop <= start:
			raise ValueError("Illegal job hours")

	def calculate_pay(self):
		current_price = self.family.price_by_hour[0][0]
		current_start_of_price = max(self.hours[0], self.family.price_by_hour[0][1])
		sum_of_costs = 0
		for price, hour_of_price_change in self.family.price_by_hour:
			if hour_of_price_change < self.hours[0] or hour_of_price_change >= self.hours[1]:
				continue
			sum_of_costs += self.calculate_hour_on_job(current_start_of_price, hour_of_price_change) * current_price
			current_price = price
			current_start_of_price = hour_of_price_change
		sum_of_costs += self.calculate_hour_on_job(current_start_of_price, self.hours[1]) * current_price
		return sum_of_costs

	def calculate_hour_on_job(self, start, stop):
		try:
			self.check_hours_validity(start, stop)
			time_on_job = stop - start
			return time_on_job.total_seconds() / 3600
		except ValueError:
			return 0