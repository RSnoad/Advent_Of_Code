from Day_5_2017 import convertToListOfDigits
from Day_5_2017 import jump
from Day_5_2017 import jumpPart2
from Test_Input import testinput
import pytest



def test_CanConvertInputToListOfDigits():
    testlist = convertToListOfDigits("0\n3\n1")
    assert testlist == [0, 3, 1]



@pytest.mark.parametrize("test_input, expected", [('0\n3\n0\n1\n-3', 5), (testinput, 343364)])
def test_CanFindNumberOfSteps(test_input, expected):
    assert jump(test_input) == expected


def test_CanFindNumberOfStepsForPart2():
    assert jumpPart2('0\n3\n0\n1\n-3') == 10
