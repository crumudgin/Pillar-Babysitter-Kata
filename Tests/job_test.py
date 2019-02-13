import pytest
from unittest import mock
from job import Job


"""
A test to ensure that the constants of the job match the requirements.
"""
@pytest.mark.parametrize(("hour"),
						[(0, 2),
						 (0, 10),
						 (2, 10),
						 (5, 6),
						 (20, 23)
						])
def test_valid_job_creation(hour):
	hours = hour
	family = mock.Mock()
	job = Job(hours, family)
	assert hours == job.hours
	assert family == job.family

@pytest.mark.parametrize(("hour"),
						[(10, 0),
						 (0, 0)
						])
def test_invalid_job_creation(hour):
	hours = hour
	family = mock.Mock()
	with pytest.raises(ValueError) as excinfo:
		job = Job(hours, family)
	assert "Illegal job hours" in str(excinfo)

