class Family():

	def __init__(self, name, price_by_hour):
		self.name = name
		self.price_by_hour = self.round_hour(price_by_hour)
		self.check_hour_validity(self.price_by_hour)

	def round_hour(self, price_and_hours):
		rounded_price_by_hour = []
		for price, time in price_and_hours:
			if time.minute != 0:
				hour = (time.hour + 1) if price == 0 else time.hour
				time = time.replace(minute=0, hour=hour)
			rounded_price_by_hour.append((price, time))
		rounded_price_by_hour.sort(key=lambda tup: tup[1])
		return rounded_price_by_hour

	def check_hour_validity(self, price_by_hour):
		for index in range(1, len(price_by_hour)):
			if price_by_hour[index][1] == price_by_hour[index-1][1]:
				raise ValueError("Illegal hours")
