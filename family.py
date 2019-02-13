from math import floor, ceil

class Family():

	def __init__(self, name, price_by_hour):
		self.name = name
		self.price_by_hour = tuple(self.round_hour(price_by_hour))

	def round_hour(self, price_and_hours):
		rounded_price_by_hour = []
		for price, hour in price_and_hours:
			rounded_hour = hour
			if hour.minute != 0:
				hour_val = hour.hour
				rounded_hour = hour.replace(minute=0, hour=((hour_val + 1) if price == 0 else hour_val))
			rounded_price_by_hour.append((price, rounded_hour))
			rounded_price_by_hour.sort(key=lambda tup: tup[1])
		return rounded_price_by_hour
