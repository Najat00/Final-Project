#Dale Nche, Emma Altenberg, Najat Abdella, Nikky Mittu

#import function
from argparse import ArgumentParser
import re
import sys
import pandas as pd

def welcome_user():
    print("\nHello! Welcome to the INST326 Movie Database! This program will allow you to view a database of movies and sort by film type and when it was released. Below you will find the database and all the movies that are in it.\n")
welcome_user()

class MovieDB:
    """
    """
    def __init__(self,filename):
        self.movie_db = pd.read_csv(filename)

    def print_movies(self): #Nikky
        """ This method reads a CSV file containing different movies and their respective information.
        Args:
            csv (str): a string containing the path to the csv file to be read.
            film (str): the type of film you are looking for (movie, documentary, etc)  
        Returns:
            A DataFrame that displays films that match your film choice.
        
        Note: It may be helpful to look at the movies.csv file to know what "filmtypes" you can choose from.
        
        """
        pd.set_option('display.max_rows', None)
        print(self.movie_db)
        print("\n")
        
    def movie_choice(self):
        self.filmtype = input("What films would you like to see? ")
        self.decade = input("\nWhat decade would you like to view films for? ")
        print("\n")
        if self.decade == "1950" and self.filmtype == "filmtype":
            a = self.movie_db[(self.movie_db["year"] >= "1950") & (self.movie_db["year"] < "1960")]
            print(a)
        elif self.decade == "1960" and self.filmtype == "filmtype":
            b = self.movie_db[(self.movie_db["year"] >= "1960") & (self.movie_db["year"] < "1970")]
            print(b)
        elif self.decade == "1970" and self.filmtype == "filmtype":
            c = self.movie_db[(self.movie_db["year"] >= "1970") & (self.movie_db["year"] < "1980")]
            print(c)
        elif self.decade == "1980" and self.filmtype == "filmtype":
            d = self.movie_db[(self.movie_db["year"] >= "1980") & (self.movie_db["year"] < "1990")]
            print(d)
        elif self.decade == "1990" and self.filmtype == "filmtype":
            e = self.movie_db[(self.movie_db["year"] >= "1990") & (self.movie_db["year"] < "2000")]
            print(e)
        elif self.decade == "2000" and self.filmtype == "filmtype":
            f = self.movie_db[(self.movie_db["year"] >= "2000") & (self.movie_db["year"] < "2010")]
            print(f)
        elif self.decade == "2010" and self.filmtype == "filmtype":
            g = self.movie_db[(self.movie_db["year"] >= "2010") & (self.movie_db["year"] < "2020")]
            print(g)
        print('\n')

def parse_args(arglist): #Nikky
    """ Parse command-line arguments """
    parser = ArgumentParser()
    parser.add_argument("filename", help="the path to the csv file")
    #parser.add_argument("filmtype", help="the type of film you want to find")
    return parser.parse_args(arglist)


if __name__ == "__main__": #Nikky
    args = parse_args(sys.argv[1:])
    movies = MovieDB(args.filename)
    movies.print_movies()
    movies.movie_choice()
