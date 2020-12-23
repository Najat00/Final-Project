from FINAL_PROJECT import age_verification
import builtins
from unittest import mock


def testo(capsys):
    """ Parameters: n/a Takes in users age and stores that value as an integer in the age variable. 
    Set conditionals to check if user is below age. 
    """
    with mock.patch('builtins.input', side_effect= ["12"]):
        assert age_verification() == "The age of 12 is to young, you'll need a parents approval to access movies in this database!\n"