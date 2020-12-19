#Dale Nche, Emma Altenberg, Najat Abdella, Nikky Mittu

from argparse import ArgumentParser
import re
import sys
import pandas as pd

def welcome_user():
    print("\nHello! Welcome to the INST326 Movie Database!")
    print("This program will allow you to view a database of movies, as well as sort by when it was released and film type.")
    print("Below you will find the database.\n")
    
welcome_user()

def age_verification():
    age = int(input("What is your age? "))
    if age < 13:
        print("You need a parents approval to access movies in this database!\n")
        exit()
    elif age > 13:
        pass

age_verification()

class MovieDB:
    """
    
    """
    def __init__(self,filename):
        """
        
        """
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
        #pd.set_option('display.max_rows', None)
        print(self.movie_db)
        
    def decade_choice(self):
        """
        
        """
        pd.set_option('display.max_rows', None)
        self.decade = input("\nWhat decade would you like to view films for? ")
        print("\n")
        if self.decade == "1950":
            a = self.movie_db[(self.movie_db["year"] >= "1950") & (self.movie_db["year"] < "1960")]
            print(a)
        elif self.decade == "1960":
            b = self.movie_db[(self.movie_db["year"] >= "1960") & (self.movie_db["year"] < "1970")]
            print(b)
        elif self.decade == "1970":
            c = self.movie_db[(self.movie_db["year"] >= "1970") & (self.movie_db["year"] < "1980")]
            print(c)
        elif self.decade == "1980":
            d = self.movie_db[(self.movie_db["year"] >= "1980") & (self.movie_db["year"] < "1990")]
            print(d)
        elif self.decade == "1990":
            e = self.movie_db[(self.movie_db["year"] >= "1990") & (self.movie_db["year"] < "2000")]
            print(e)
        elif self.decade == "2000":
            f = self.movie_db[(self.movie_db["year"] >= "2000") & (self.movie_db["year"] < "2010")]
            print(f)
        elif self.decade == "2010":
            g = self.movie_db[(self.movie_db["year"] >= "2010") & (self.movie_db["year"] < "2020")]
            print(g)
        print('\n')
        
    def movie_type(self):
        """
        
        """
        pd.set_option('display.max_rows', None)
        self.filmtype = input("What films would you like to see? ")
        print("\n")
        if self.filmtype == "Movie":
            m = self.movie_db[(self.movie_db["filmtype"] == "Movie")]
            print(m)
        elif self.filmtype == "Documentary":
            d = self.movie_db[(self.movie_db["filmtype"] == "Documentary")]
            print(d)
        elif self.filmtype == "TV-S":
            tvs = self.movie_db[(self.movie_db["filmtype"] == "TV-S")]
            print(tvs)
        elif self.filmtype == "TV-M":
            tvm = self.movie_db[(self.movie_db["filmtype"] == "TV-M")]
            print(tvm)
        elif self.filmtype == "Short":
            s = self.movie_db[(self.movie_db["filmtype"] == "Short")]
            print(s)
        print('\n')

def parse_args(arglist): #Nikky
    """ Parse command-line arguments """
    parser = ArgumentParser()
    parser.add_argument("filename", help="the path to the csv file")
    return parser.parse_args(arglist)


if __name__ == "__main__": #Nikky
    args = parse_args(sys.argv[1:])
    movies = MovieDB(args.filename)
    movies.print_movies()
    movies.decade_choice()
    movies.movie_type()
