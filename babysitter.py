from functools import reduce
from datetime import datetime

class Babysitter():
	
	def __init__(self, earliest_start_time = datetime(2019, 2, 13, 17), latest_end_time = datetime(2019, 2, 14, 4), max_jobs = 1):
		self.earliest_start_time = earliest_start_time
		self.latest_end_time = latest_end_time
		self.max_jobs = max_jobs
		self.jobs = []

	def take_job(self, job):
		if len(self.jobs) >= self.max_jobs:
			raise ValueError("The babysitter is only axxepting %d job(s) per night" %self.max_jobs)
		for _, hour in job.hours:
			if hour < self.earliest_start_time or hour > self.latest_end_time:
				raise ValueError("The babysitter works from %d - %d" %(self.earliest_start_time.hour, self.latest_end_time.hour))
		self.jobs.append(job)
			
	def calc_earnings(self):
		earnings = sum(map(lambda job: job.calc_earnings, self.jobs))
		return earnings if earnings else 0