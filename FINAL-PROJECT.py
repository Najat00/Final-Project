#Dale Nche, Emma Altenberg, Najat Abdella, Nikky Mittu

#import function
from argparse import ArgumentParser
import re
import sys
from #insert file name# import #class, function(s)

#Nikky 
class Movie_Generator: #class
"""This module reads in a text file with movies and their relevant information. 
It then returns a list of movies that meets the requirements of the information specified by the user
Args:
title (str): the title of the film
film_type (str): the type of film 
director (str): the director of the film
rating (float): the rating of the film 0.0-10.0
runtime (int): the duration of the film in minutes
year (int): the year the film was released
genre (str): the genre of the film 
Returns:
a list of movies that meets the requirements of the information put into the generator"""

	def __init__(self, title, film_type, director, rating, runtime, year, genre): #init method
"""This method initializes information about the move. 
The parameters are self, title, filmtype,author, rating, runtime, year, genre."""

#attributes
self.title = title
self.film_type = filmtype
self.director = director
self.rating = rating
self.runtime = runtime
self.year = year
self.genre = genre

#Najat
class Restriction(Movie_generator): #subclass and using the super() function
"""A class that puts a restriction on the Genre of Horror and Thriller using the super() function”””
    Attributes(str):
        age(int): value between 0-12  inclusive
        Genre(str): imported from self.genre, genre of the movie

    Methods:
        __init__()
        __str__()
"""

#Dale's
#opening file function 
"""Responsible for creating key values for Movie title, genres and Film type
Parameters: self, filename
Filename: name of movie txt filename """

def parse_args(arglist): #utilizing the parse function
    """ Parse command line arguments.
    
    Arguments:
        arglist """

#Emma’s headers and docstrings (3, 4):
def read_text(self, filename):
"""
Purpose is to read the file and use the information to create 
the Movie_Generator class
Attributes: filename(str): the name of the text file containing the movie information
Returns: a list of results of the movies in the file given
"""
def read_text():
    self.results=[]
    with open(filename, "r", encoding="utf-8") as f:
        for line in r:
            strip=line.strip()
            split=line.spliy(";")
            movie=split[0]
            film_type=split[1]
            director=split[2]
            ratings=split[3]
            run_time=split[4]
            year=split[5]
            genre=split[6]
            results.append(Movie_Generator(movie, film_type, director,
                                           ratings, run_time, year, genre))
    return self.results
            
def year_generate(input):
    """
    Purpose: Generates a list of movies from a users desired decade to choose from 
    Attributes: input(str): the information that the user answered with
    Returns: a list of movies from the decade that the user asks for
    """
    if input= "1950":
        return year>1949 and year<1960
    elif input="1960":
        return year>1959 and year<1970
    elif input="1970":
        return year>1969 and year<1980
    elif input="1980":
        return year>1979 and year<1990
    elif input="1990":
        return year>1989 and year<2000
    elif input="2000":
        return year>1999 and year<2010
    elif input="2010":
        return year>2000
    else:
        raise ValueError("Enter a decade between 1950 and 2010")