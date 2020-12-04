#Dale Nche, Emma Altenberg, Najat Abdella, Nikky Mittu

#import function
from argparse import ArgumentParser
import re
import sys

def movie_database(csv, film): #Nikky
    """ This method reads a CSV file containing different movies and their respective information.
    Args:
        csv (str): a string containing the path to the csv file to be read.
        film (str): the type of film you are looking for (movie, documentary, etc)  
    Returns:
        A DataFrame that displays films that match your film choice.
    
    Note: It may be helpful to look at the movies.csv file to know what filmtypes you can choose from.
    
    """
    pd.set_option('display.max_rows', None)
    df = pd.read_csv(csv)
    print(df[df["filmtype"]== film])

def parse_args(arglist): #Nikky
    """ Parse command-line arguments """
    parser = ArgumentParser()
    parser.add_argument("csv", help="the path to the csv file")
    parser.add_argument("film", help="the type of film you want to find")
    return parser.parse_args(arglist)


if __name__ == "__main__": #Nikky
    args = parse_args(sys.argv[1:])
    movie_database(args.csv, args.film)

#Najat
def __init__(self,age, genre):
        self.age = age
        self.genre = genre
user_age= int(input("What is your age?"))
    if user_age < 12:
        return ("You are not of age to watch this movie")
      
#Dale's
#opening file function 
"""Responsible for creating key values for Movie title, genres and Film type
Parameters: self, filename
Filename: name of movie txt filename """

def parse_args(arglist): #utilizing the parse function
    """ Parse command line arguments.
    
    Arguments:
        arglist """
#1) Use Pandas to print out a graphical representation of the txt file (Pandas and args)
    #2) Focus on opening the txt file and reading it in ( read txt file and parse)
    #3) Parse the txt file and sort based upon genre and year
    #4) completed dict that has each movie title stored as an individual key and addiional info 
    stored as values ( generate dict and sort data)
    #5) input function requesting age/genre/ and or year( input and generate conditionals)
    #6) use input data to fetch user recommendations (conditionals and return results) """
#Emma’s headers and docstrings (3, 4):
def read_text(self, filename):
"""
Purpose is to read the file and use the information to create 
the Movie_Generator class
Attributes: filename(str): the name of the text file containing the movie information
Returns: a list of results of the movies in the file given
"""
    self.results=[]
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            strip=line.strip()
            split=line.spliy(";")
            movie=split[0]
            film_type=split[1]
            director=split[2]
            ratings=split[3]
            run_time=split[4]
            year=split[5]
            genre=split[6]
            results.append(movie, film_type, director,
                                           ratings, run_time, year, genre))
    return self.results
            
def year_generate(input):
    """
    Purpose: Generates a list of movies from a users desired decade to choose from 
    Attributes: input(str): the information that the user answered with
    Returns: a list of movies from the decade that the user asks for
    Raises:
    Value Error if year is not between 1950 and 2010
    """
    #Najat  
    yeartype = int(input("What decade would you like to watch a movie from? "))
    return # a list of movies from that year
    #Emma
    if yeartype= "1950":
        return year>1949 and year<1960
    elif yeartype="1960":
        return year>1959 and year<1970
    elif yeartype="1970":
        return year>1969 and year<1980
    elif yeartype="1980":
        return year>1979 and year<1990
    elif yeartype="1990":
        return year>1989 and year<2000
    elif yeartype="2000":
        return year>1999 and year<2010
    elif yeartype="2010":
        return year>2000
    else:
        raise ValueError("Enter a decade between 1950 and 2010")
 
    