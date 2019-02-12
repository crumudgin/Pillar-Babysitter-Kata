from math import floor, ceil

class Family():

	def __init__(self, name, price_by_hour):
		self.name = name
		self.price_by_hour = tuple(self.round_hour(price_by_hour))

	def round_hour(self, price_and_hours):
		rounded_price_by_hour = []
		for price, hour in price_and_hours:
			rounded_hour = ceil(hour) if price == 0 else floor(hour)
			rounded_price_by_hour.append((price, rounded_hour))
		return rounded_price_by_hour
