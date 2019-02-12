import pytest
from babysitter import Babysitter
from job import Job
from datetime import time

"""
user stories:
As a babysitter
In order to get paid for 1 night of work
I want to calculate my nightly charge
"""

"""
The babysitter:
starts no earlier than 5:00PM
leaves no later than 4:00AM
only babysits for one family per night
gets paid for full hours
should be prevented from mistakes when entering times(e.g. end time before start time, or outside of allowable work hours)
"""

@pytest.fixture
def babysitter():
	return Babysitter()

"""
A test to ensure that the constants of the babysitter match the requirements.
"""
def test_babysitter_constants(babysitter):
	assert babysitter.earliest_start_time == time(hour=17)
	assert babysitter.latest_end_time == time(hour=4)
	assert babysitter.max_jobs == 1

"""
A test to ensure that the constants of the job match the requirements.
"""
def test_job_constants():
	hours = []
	job = Job(hours)
	assert job.earliest_start_time == time(hour=17)
	assert job.latest_end_time == time(hour=4)