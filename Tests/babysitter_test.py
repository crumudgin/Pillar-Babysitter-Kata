import pytest
import sys
from unittest import mock
from babysitter import Babysitter
from datetime import datetime
from helper_functions import *


@pytest.fixture
def babysitter():
	return Babysitter()


def test_babysitter_constants(babysitter):
	"""
	A test to ensure that the constants of the babysitter match the requirements.
	"""
	assert babysitter.earliest_start_time == datetime(2019, 2, 13, 17)
	assert babysitter.latest_end_time == datetime(2019, 2, 14, 4)
	assert babysitter.max_jobs == 1


@pytest.mark.parametrize(("hours"),
						[((0, 0), (0, 11)),
						 ((0, 1), (0, 11)),
						 ((0, 1), (0, 8)),
						 ((0, 5), (0, 11)),
						 ((0, 0), (0, 5), (0, 11)),
						 ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11))
						])
def test_babysitter_take_valid_job(babysitter, hours):
	job = mock.Mock()
	job.configure_mock(hours=convert_price_hour_tuples(hours))
	babysitter.take_job(job)
	assert babysitter.jobs == [job]


@pytest.mark.parametrize(("hours"),
						[((0, 0), (0, 12)),
						 ((0, 13), (0, 14)),
						 ((0, -1), (0, 1))
						])
def test_babysitter_take_invalid_job(babysitter, hours):
	job = mock.Mock()
	job.configure_mock(hours=convert_price_hour_tuples(hours))
	with pytest.raises(ValueError) as excinfo:
		babysitter.take_job(job)
	time_tuple = (babysitter.earliest_start_time.hour, babysitter.latest_end_time.hour)
	assert "The babysitter works from %d - %d" %time_tuple in str(excinfo)
	assert babysitter.jobs == []


def test_babysitter_add_multiple_jobs(babysitter):
	job1 = mock.Mock()
	job2 = mock.Mock()
	job1.configure_mock(hours=(convert_price_hour_tuples(((0, 1), (0, 2)))))
	babysitter.take_job(job1)
	with pytest.raises(ValueError) as excinfo:
		babysitter.take_job(job2)
	assert "The babysitter is only accepting %d job(s) per night" %babysitter.max_jobs in str(excinfo)
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

