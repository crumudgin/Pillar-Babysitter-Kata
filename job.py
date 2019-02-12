from datetime import time

class Job():

	def __init__(self, hours, earliest_start_time = time(hour=17), latest_end_time = time(hour=4)):
		self.earliest_start_time = earliest_start_time
		self.latest_end_time = latest_end_time
		self.hours = hours