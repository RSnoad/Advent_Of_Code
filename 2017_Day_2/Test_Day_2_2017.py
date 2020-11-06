from Day_2_2017 import difference
from Day_2_2017 import checksum
from Day_2_2017 import evendivision
from Day_2_2017 import divisionsum
import pytest

@pytest.mark.parametrize("test_input,expected", [("5 1 9 5", 8), ("7 5 3", 4), ("2 4 6 8", 6) ])
def test_CanCalculateDifferenceBetweenMaxAndMinInRow(test_input, expected):
    assert difference(test_input) == expected


def test_ChecksumIsCalculatedCorrectly():
    assert checksum("5 1 9 5", "7 5 3", "2 4 6 8") == 18


@pytest.mark.parametrize("test_input,expected", [("5 9 2 8 ", 4), ("9 4 7 3", 3), ("3 8 6 5", 2)])
def test_CanFindTheOnlyEvenlyDivisiblePairAndReturnDivisionResult(test_input, expected):
    assert evendivision(test_input) == expected


def test_CanSumTheResultOfTheEvenlyDividedPairs():
    assert divisionsum("5 9 2 8", "9 4 7 3", "3 8 6 5") == 9
