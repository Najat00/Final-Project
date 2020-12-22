from FINAL_PROJECT import __init__, print_movies
import pytest
#Najat
def test_init():
   """" Tests the __init__() method of the MovieDB class and has the correct amount of rows"""
if len(self.movie_db.columns) == 7:
    pass
else:
    exit()
    

def test_print_movies(capsys):
    """Test the print_movies() method of the MovieDB class."""
    captured= capsys.readouterr()
    captured.out == "movie_db.\n"
    
    
    