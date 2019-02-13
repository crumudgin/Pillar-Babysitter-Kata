from datetime import datetime, timedelta

def convert_hour_to_time(hour):
	# I just went with todays date because the resolution specified in the assignment is for one night
	base_time = datetime(2019, 2, 13, 17)
	minute = round((hour % 1) * 100)
	hour = hour // 1
	hourdelta = timedelta(hours = hour, minutes = minute)
	return base_time + hourdelta

def convert_price_hour_tuples(tup):
	range_of_hours = [(price, convert_hour_to_time(hour)) for price, hour in tup]
	return tuple(range_of_hours)