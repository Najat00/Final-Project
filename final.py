#Dale Nche, Emma Altenberg, Najat Abdella, Nikky Mittu

#import function
from argparse import ArgumentParser
import re
import sys
from #insert file name# import #class, function(s)#

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
Purpose is to run through and read the text file that contains the movie information in it
Attributes: filename(dic): the text file containing the movie information
Returns: a dictionary of movies which includes each movies individual directors, runtimes, ratings, year of release, genre, and type of film
"""
#strip function
def strip_text(self, filename):
"""
Purpose is to remove unwanted grammar marks, spaces, and other objects so that our code runs and returns information as smoothly as possible 
Attributes: filename(dic): the text file containing the movie information
Returns: list from the movie text file that is striped of all unwanted grammer objects
"""
