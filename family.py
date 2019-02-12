from math import floor, ceil

class Family():

	def __init__(self, name, price_by_hour):
		self.name = name
		temp_lst = []
		for price, hour in price_by_hour:
			rounded_hour = ceil(hour) if price == 0 else floor(hour)
			temp_lst.append((price, rounded_hour))
		self.price_by_hour = tuple(temp_lst)