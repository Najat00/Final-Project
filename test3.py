#David McCoy and Dale Nche

from fp import age_verification
import builtins
from unittest import mock


def testo(capsys):
    with mock.patch('builtins.input', side_effect= ["12"]):
        assert age_verification() == "The age of 12 is to young, you'll need a parents approval to access movies in this database!\n"