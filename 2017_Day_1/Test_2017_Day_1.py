import pytest
from Day_1_2017 import captchaDefinedStep

@pytest.mark.parametrize("test_input, test_step, expected", [("1122", 1, 3), ("1234", 1, 0)])
def test_Part1SumIsCalculatedCorrectlyForNonCircularSequence(test_input, test_step, expected):
    assert captchaDefinedStep(test_input, test_step) == expected

@pytest.mark.parametrize("test_input, test_step, expected", [("1111", 1, 4), ("91212129", 1, 9)])
def test_Part1SumIsCalculatedCorrectlyForCircularSequence(test_input, test_step, expected):
    assert captchaDefinedStep(test_input, test_step) == expected

@pytest.mark.parametrize("test_input,expected", [("1212", 6), ("1221", 0), ("123123", 12), ("12131415", 4)])
def test_Part2SumIsCalculatedCorrectly(test_input, expected):
    step = int((len(test_input) / 2))
    assert captchaDefinedStep(test_input, step) == expected
