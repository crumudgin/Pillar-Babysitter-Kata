class Job():

	def __init__(self, hours, earliest_start_time = 0, latest_end_time = 10):
		self.earliest_start_time = earliest_start_time
		self.latest_end_time = latest_end_time
		self.hours = hours