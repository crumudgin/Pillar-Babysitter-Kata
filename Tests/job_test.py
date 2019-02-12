import pytest
from job import Job


"""
A test to ensure that the constants of the job match the requirements.
"""
def test_job_constants():
	hours = []
	job = Job(hours)
	assert job.earliest_start_time == 0
	assert job.latest_end_time == 10