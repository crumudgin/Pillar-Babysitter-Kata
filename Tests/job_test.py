import pytest
from unittest import mock
from job import Job


"""
A test to ensure that the constants of the job match the requirements.
"""
def test_job_creation():
	hours = []
	family = mock.Mock()
	job = Job(hours, family)
	assert hours == job.hours
	assert family == job.family

