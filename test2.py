from FINAL_PROJECT import MovieDB, __init__
import pytest
#Najat
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
    captured= capsys.readouterr()
    captured.out == "movie_db.\n"
    
    
    