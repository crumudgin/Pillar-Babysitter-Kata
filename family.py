from math import floor, ceil

class Family():

	def __init__(self, name, price_by_hour):
		self.name = name
		temp_lst = []
		for price, hour in price_by_hour:
			if price == 0:
				temp_lst.append((price, ceil(hour)))
			else:
				temp_lst.append((price, floor(hour)))
		self.price_by_hour = tuple(temp_lst)