from functools import reduce

class Babysitter():
	
	def __init__(self, earliest_start_time = 0, latest_end_time = 10, max_jobs = 1):
		self.earliest_start_time = earliest_start_time
		self.latest_end_time = latest_end_time
		self.max_jobs = max_jobs
		self.jobs = []

	def take_job(self, job):
		if len(self.jobs) >= self.max_jobs:
			raise ValueError("The babysitter is only axxepting %d job(s) per night" %self.max_jobs)
		for start, stop in job.hours:
			if min(start, stop) < self.earliest_start_time or max(start, stop) > self.latest_end_time:
				raise ValueError("The babysitter starts no earlier than %d and ends no later than %d" %(self.earliest_start_time, self.latest_end_time))
		self.jobs.append(job)
			
	def calc_earnings(self):
		earnings = sum(map(lambda job: job.calc_earnings, self.jobs))
		return earnings if earnings else 0