from argparse import ArgumentParser
import pandas as pd
import sys

def movie_database(csv, film):
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

def parse_args(arglist):
    """ Parse command-line arguments """
    parser = ArgumentParser()
    parser.add_argument("csv", help="the path to the csv file")
    parser.add_argument("film", help="the type of film you want to find")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movie_database(args.csv, args.film)