#Dale Nche, Emma Altenberg, Najat Abdella, Nikky Mittu

#import function
from argparse import ArgumentParser
import re
import sys
import pandas as pd

#class MovieDB:
    #will be implemented after rearranging functions


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

#Najat
def __init__(self,name, year):
    user_name = input("Hi! What is your name? ")
    self.name = user_name
    year = input("What decade would you like to watch a movie from? ")
    self.year = int(year)

def read_text(self, filename):
    """
    Purpose is to read the file and use the information to create 
    the Movie_Generator class
    Attributes: 
        filename(str): the name of the text file containing the movie information
    Returns: 
    a list of results of the movies in the file given"""
    #self.results=[]
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            split=line.split(",")
            title=split[0]
            filmtype=split[1]
            director=split[2]
            ratings=split[3]
            duration=split[4]
            year1 =split[5]
            genre=split[6]
            #self.results.append(title, filmtype, director, ratings, duration, year, genre)
       #return self.results

def movie_pair(self, filename):
    """Responsible for creating key values for Movie year
    EX: dict1{Action: IronMan, Hulk, Assasin} essentially dicionaries based on genre
    then based of users input we move onto 
    dic2{IronMan: etc, etc, etc}
    dic3{}
    Parameters: self, filename
    Filename: name of movie txt filename """
#Emma’s headers and docstrings (3, 4):


            
def year_generate():
    """
    Purpose: Generates a list of movies from a users desired decade to choose from 
    Attributes: input(str): the information that the user answered with
    Returns: a list of movies from the decade that the user asks for
    Raises:
    Value Error if year is not between 1950 and 2010
    """
    #Emma
    if year == "1950":
        return year>1949 and year<1960
    elif year=="1960":
        return year>1959 and year<1970
    elif year=="1970":
        return year>1969 and year<1980
    elif year=="1980":
        return year>1979 and year<1990
    elif year=="1990":
        return year>1989 and year<2000
    elif year=="2000":
        return year>1999 and year<2010
    elif year=="2010":
        return year>2000
    else:
        raise ValueError("Enter a decade between 1950 and 2010")
 
def parse_args(arglist): #Nikky
    """ Parse command-line arguments """
    parser = ArgumentParser()
    parser.add_argument("csv", help="the path to the csv file")
    parser.add_argument("film", help="the type of film you want to find")
    return parser.parse_args(arglist)


if __name__ == "__main__": #Nikky
    args = parse_args(sys.argv[1:])
    movie_database(args.csv, args.film)
