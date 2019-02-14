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

@pytest.mark.parametrize(("hours", "pay", 								"expected_output"),
						[((0, 10),	((1, 0),),							10),#test that the function calculates the hours for a single pay range
						 ((0, 10),	((2, 0),),							20),#test that the function works for multiple inputs
						 ((0, 10),	((1, 0), (2, 5)),					15),#test that the function works with multiple time ranges
						 ((2, 8),	((2, 0), (3, 5)),					15),#test that the function works for any legal hour range
						 ((0, 10),	((2, 2), (4, 5)),					26),#test the outcome when the pay starts later than the hours
						 ((0, 10),	((5, 0), (0, 5)),					25),#test the outcome when the pay stops earlier than the hours
						 ((0, 4),	((1, 0), (2, 1), (3, 2), (4, 3)),	10)	#test the output with many different pay ranges
						])
def test_calculate_pay(hours, pay, expected_output):
	family = mock.Mock()
	family.price_by_hour=convert_price_hour_tuples(pay)
	hours = tuple((convert_hour_to_time(hour) for hour in hours))
	job = Job(hours, family)
	assert job.calculate_pay() == expected_output

