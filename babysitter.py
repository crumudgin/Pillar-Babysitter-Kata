from functools import reduce
from datetime import datetime


class Babysitter():

	def __init__(self,
				 earliest_start_time=datetime(2019, 2, 13, 17),
				 latest_end_time=datetime(2019, 2, 14, 4),
				 max_jobs=1
				):

		self.earliest_start_time = earliest_start_time
		self.latest_end_time = latest_end_time
		self.max_jobs = max_jobs
		self.jobs = []

	def take_job(self, job):
		if len(self.jobs) >= self.max_jobs:
			error_txt = "The babysitter is only accepting %d job(s) per night" %self.max_jobs
			raise ValueError(error_txt)
		for _, hour in job.hours:
			if hour < self.earliest_start_time or hour > self.latest_end_time:
				time_tuple = (self.earliest_start_time.hour, self.latest_end_time.hour)
				raise ValueError("The babysitter works from %d - %d" %time_tuple)
		self.jobs.append(job)

	def calc_earnings(self):
		earnings = sum(map(lambda job: job.calc_earnings, self.jobs))
		return earnings if earnings else 0
