from datetime import time

class Babysitter():
	
	def __init__(self, earliest_start_time = time(hour=17), latest_end_time = time(hour=4), max_jobs = 1):
		self.earliest_start_time = earliest_start_time
		self.latest_end_time = latest_end_time
		self.max_jobs = max_jobs