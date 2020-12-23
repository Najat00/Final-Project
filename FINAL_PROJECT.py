#Dale Nche, Emma Altenberg, Najat Abdella, Nikeet Mittu
#Movie Database

from argparse import ArgumentParser
import re
import sys
import pandas as pd

def welcome_user():
    """ This function welcomes the user and explains the purpose of the program. 
    It prints out the following messages before running the rest of the program. """
    
    print("\nHello! Welcome to the INST326 Movie Database!")
    print("This program will allow you to view a database of movies, as well as sort by when it was released and film type.")
    print("Below you will find the database.\n")

    
def age_verification():
    """ This function verifies the age of the user. 
    If the user is under the age of 13, the program terminates, as some movies in the database may not be suitable for younger users.
    Otherwise, the program will move on to the next function. """
    
    age = int(input("What is your age? "))
    if age < 13:
        sys.exit(f"\nThe age of {age} is to young. You'll need a parents approval to access movies in this database!\n")
    elif age >= 13:
        pass


class MovieDB:
    """ A class that allows users to select a movie according to decade and filmtype
    Attributes:
        filename: a path to the .csv file to be read in
    Methods:
        __init__(), print_movies(), decade_choice(), movie_type() """
    
    def __init__(self,filename):
        """ This function sets the parameters for filename reads and establishes a movie database 
        Args:
            filename: a path to the .csv file to be read in. """
        self.movie_db = pd.read_csv(filename)

    def print_movies(self):
        """ This method turns the information in the .csv file into a dataframe.
 
        Returns:
            A DataFrame that displays films in the .csv file.
        
        Note: It may be helpful to look at the movies.csv file to know what "filmtypes" are present in the file.
        
        """
        
        print(self.movie_db)
        
    def decade_choice(self):
        """ This method prompts the user to enter the decade that they would like to view films from. It then returns a dataframe with only films created 
        in that decade.
        Args:
            decade: a decade specified by the user
        Returns:
            A dataframe with only films from that decade
        
        """
        pd.set_option('display.max_rows', None)
        self.decade = input("\nWhat decade would you like to view films for? Select a decade a between 1950 and 2010: ")

        if self.decade == "1950":
            return self.movie_db[(self.movie_db["year"] >= "1950") & (self.movie_db["year"] < "1960")]
        elif self.decade == "1960":
            return self.movie_db[(self.movie_db["year"] >= "1960") & (self.movie_db["year"] < "1970")]
        elif self.decade == "1970":
            return self.movie_db[(self.movie_db["year"] >= "1970") & (self.movie_db["year"] < "1980")]
        elif self.decade == "1980":
            return self.movie_db[(self.movie_db["year"] >= "1980") & (self.movie_db["year"] < "1990")]
        elif self.decade == "1990":
            return self.movie_db[(self.movie_db["year"] >= "1990") & (self.movie_db["year"] < "2000")]
        elif self.decade == "2000":
            return self.movie_db[(self.movie_db["year"] >= "2000") & (self.movie_db["year"] < "2010")]
        elif self.decade == "2010":
            return self.movie_db[(self.movie_db["year"] >= "2010") & (self.movie_db["year"] < "2020")]

        return None
        
    def movie_type(self):
        """ This method prompts the user to enter the type of film that they would like to view. It then returns a dataframe with only films that are in the
        category specified by the user.
        Args:
            filmtype: the type of film, as specified by the user
        Returns:
            A dataframe with only the specific filmtype specified.
        
        """
        pd.set_option('display.max_rows', None)
        self.filmtype = input("What films would you like to see? ")

        if self.filmtype == "Movie":
            return self.movie_db[(self.movie_db["filmtype"] == "Movie")]
        elif self.filmtype == "Documentary":
            return self.movie_db[(self.movie_db["filmtype"] == "Documentary")]
        elif self.filmtype == "TV-S":
            return self.movie_db[(self.movie_db["filmtype"] == "TV-S")]
        elif self.filmtype == "TV-M":
            return self.movie_db[(self.movie_db["filmtype"] == "TV-M")]
        elif self.filmtype == "Short":
            return self.movie_db[(self.movie_db["filmtype"] == "Short")]

def parse_args(arglist):
    """ Parse command-line arguments """
    if not arglist:
        raise ValueError("no arguments")
    parser = ArgumentParser()
    parser.add_argument("filename", help="the path to the csv file")
    return parser.parse_args(arglist)


if __name__ == "__main__": 
    args = parse_args(sys.argv[1:])
    welcome_user()
    age_verification()
    movies = MovieDB(args.filename)
    movies.print_movies()
    decade = movies.decade_choice()
    print(decade, "\n")
    movie_types = movies.movie_type()
    print(movie_types, "\n")