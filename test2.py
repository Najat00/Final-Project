from FINAL_PROJECT import MovieDB, __init__
from unittest import mock
import pandas as pd

def test_init():
    """" Tests the __init__() method of the MovieDB class and has the 
correct amount of columns
""" 
mdb = MovieDB("movies.csv")
if len(mdb.movie_db.columns) == 7:
    pass
else:
    exit()

def test_print_movies(capsys):
    """Test the print_movies() method of the MovieDB class."""
with mock.patch("builtins.input",
                    side_effect=["11"]):
    m = MovieDB("movies.csv")
    assert m.print_movies() == print(pd.read_csv("movies.csv"))
    
    
    
    