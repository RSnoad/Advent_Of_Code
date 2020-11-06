import pytest
from Day_4_2017 import passPhraseValidator
from Day_4_2017 import isAnagram
from Day_4_2017 import anagramPassphraseValidator

@pytest.mark.parametrize("test_input", ["aa bb cc dd ee", "aa bb cc dd aaa"])
def test_CanCheckAValidPassphrase(test_input):
    assert passPhraseValidator(test_input)

def test_CanRejectInvalidPassphrase():
    assert not passPhraseValidator("aa bb cc dd aa")


def test_CanIdentifyAnagram():
    assert isAnagram("abcde","edbca")

def test_CanIdentifyNonAnagram():
    assert not isAnagram("abcde", "fghij")

@pytest.mark.parametrize("test_input", ["abcde fghij", "a ab abc abd abf abj", "iiii oiii ooii oooi oooo"])
def test_CanCheckAValidPassphraseWithNoAnagramRequirement(test_input):
    assert anagramPassphraseValidator(test_input)

@pytest.mark.parametrize("test_input", ["abcde xyz ecdab", "oiii ioii iioi iiio"])
def test_CanRejectAValidPassphraseWithNoAnagramRequirement(test_input):
    assert not anagramPassphraseValidator(test_input)