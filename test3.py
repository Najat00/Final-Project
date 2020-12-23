from FINAL_PROJECT import age_verification
import builtins
from unittest import mock
import pytest

def test_underage(capsys):
    """ Parameters: n/a Takes in users age and stores that value as an integer in the age variable. 
    Set conditionals to check if user is below age. 
    """
    with mock.patch('builtins.input', side_effect= ["12"]):
        with pytest.raises(SystemExit):
            assert age_verification() == ("The age of {age} is to young, you'll need a parents approval to access movies in this database!\n")
    with mock.patch('builtins.input', side_effect= ["10"]):
        with pytest.raises(SystemExit):
            assert age_verification() == ("The age of {age} is to young, you'll need a parents approval to access movies in this database!\n")
    with mock.patch('builtins.input', side_effect= ["8"]):
        with pytest.raises(SystemExit):
            assert age_verification() == ("The age of {age} is to young, you'll need a parents approval to access movies in this database!\n")

def test_ofAge(capsys):
    with mock.patch('builtins.input', side_effect= ["21"]):
        try:
            age_verification()
        except SystemExit:
            pytest.fail("Unexpected SystemExit")
    with mock.patch('builtins.input', side_effect= ["13"]): #test edge case
        try:
            age_verification()
        except SystemExit:
            pytest.fail("Unexpected SystemExit")
    with mock.patch('builtins.input', side_effect= ["46"]):
        try:
            age_verification()
        except SystemExit:
            pytest.fail("Unexpected SystemExit")
        
