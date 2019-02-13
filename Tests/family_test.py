import pytest
from family import Family
from datetime import datetime
from helper_functions import *


@pytest.mark.parametrize(("name",			"hours",					"expected_hours"),
						[("whole_number",	((15,0),(30,5),(0,7)),			((15,0), (30,5),(0,7))),
						 ("decimal_number",	((15,0.3),(40,5.59),(0,7.1)),	((15,0), (40,5),(0,8))),
						 ("unsorted",		((15,10),(20,0)),				((20,0), (15,10)))
						])
def test_family_creation(name, hours, expected_hours):
	converted_hour = convert_price_hour_tuples(hours)
	family = Family(name, converted_hour)
	assert family.name == name
	assert family.price_by_hour == convert_price_hour_tuples(expected_hours)