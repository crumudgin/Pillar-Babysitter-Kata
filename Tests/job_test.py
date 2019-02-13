import pytest
from unittest import mock
from job import Job
from datetime import datetime
from helper_functions import *

@pytest.fixture
def family():
	family = mock.Mock()

"""
A test to ensure that the constants of the job match the requirements.
"""
@pytest.mark.parametrize(("hours"),
						[(0, 2),
						 (0, 10),
						 (2, 10),
						 (5, 6),
						 (20, 23)
						])
def test_valid_job_creation(family, hours):
	hours = tuple((convert_hour_to_time(hour) for hour in hours))
	job = Job(hours, family)
	assert hours == job.hours
	assert family == job.family

@pytest.mark.parametrize(("hours"),
						[(10, 0),
						 (0, 0)
						])
def test_invalid_job_creation(family, hours):
	hours = tuple((convert_hour_to_time(hour) for hour in hours))
	with pytest.raises(ValueError) as excinfo:
		job = Job(hours, family)
	assert "Illegal job hours" in str(excinfo)

