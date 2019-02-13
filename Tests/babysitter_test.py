import pytest
import sys
from unittest import mock
from babysitter import Babysitter


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
	assert babysitter.earliest_start_time == 0
	assert babysitter.latest_end_time == 10
	assert babysitter.max_jobs == 1

@pytest.mark.parametrize(("hours"),
						[((0, 0), (0, 10)),
						 ((0, 1), (0, 10)),
						 ((0, 1), (0, 8)),
						 ((0, 5), (0, 10)),
						 ((0, 0), (0, 5), (0, 10)),
						 ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10))
						])
def test_babysitter_take_valid_job(babysitter, hours):
	job = mock.Mock()
	job.configure_mock(hours=hours)
	babysitter.take_job(job)
	assert babysitter.jobs == [job]


@pytest.mark.parametrize(("hours"),
						[((0, 0), (0, 11)),
						 ((0, 11), (0, 12)),
						 ((0, -1), (0, 1))
						])
def test_babysitter_take_invalid_job(babysitter, hours):
	job = mock.Mock()
	job.configure_mock(hours=hours)
	with pytest.raises(ValueError) as excinfo:
		babysitter.take_job(job)
	error_msg = "The babysitter starts no earlier than %d and ends no later than %d" %(babysitter.earliest_start_time, babysitter.latest_end_time)
	assert error_msg in str(excinfo)
	assert babysitter.jobs == []

def test_babysitter_add_multiple_jobs(babysitter):
	job1 = mock.Mock()
	job2 = mock.Mock()
	job1.configure_mock(hours=((0, 1), (0, 2)))
	babysitter.take_job(job1)
	with pytest.raises(ValueError) as excinfo:
		babysitter.take_job(job2)
	assert "The babysitter is only axxepting %d job(s) per night" %babysitter.max_jobs in str(excinfo)
	assert babysitter.jobs == [job1]


@pytest.mark.parametrize(("earnings"),
						[(0),
						 (1),
						 (2),
						 (sys.maxsize)
						])
def test_babysitter_calc_earnings(babysitter, earnings):
	job = mock.Mock()
	job.configure_mock(calc_earnings=earnings)
	babysitter.jobs = [job]
	assert earnings == babysitter.calc_earnings()

def test_babysitter_calc_earnings_no_jobs(babysitter):
	assert babysitter.calc_earnings() == 0

