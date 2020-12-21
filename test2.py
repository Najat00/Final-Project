from FINAL_PROJECT import print_movies
import pytest
#Najat
#def test_init():
   # """" Tests the __init__() method of the MovieDB class."""

#movie =MovieDB()


def test_print_movies(capsys):
    """Test the print_movies() method of the MovieDB class."""
    captured= capsys.readouterr()
    captured.out == "movie_db.\n"
    
    
    