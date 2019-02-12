import pytest
from family import Family


@pytest.mark.parametrize(("name",			"hours",					"expected_hours"),
						[("whole_number",	((15,0),(30,5),(0,7)),		((15,0), (30,5),(0,7))),
						 ("decimal_number",	((15,0.3),(40,5.9),(0,7.1)),((15,0), (40,5),(0,8)))
						])
def test_family_creation(name, hours, expected_hours):
	family = Family(name, hours)
	assert family.name == name
	assert family.price_by_hour == expected_hours