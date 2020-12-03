from argparse import ArgumentParser
import pandas as pd
import sys

def movie_database(csv, film):
    """ This method reads a CSV file containing different movies and their respective information.
    Args:
        csv (str): a string containing the path to the csv file to be read.
        film (str): the type of film you are looking for (movie, documentary, etc)  
    Returns:
        TBD
    """
    df = pd.read_csv(csv)
    print(df)
    fil = df[df["film"] == film]
    cols1 = "rating"
    cols = fil[cols1].max()
    duration = fil[fil[cols1]==cols]["duration"]
    top_movies = duration.iloc[0]
    return (top_movies, cols)

def parse_args(arglist):
    """ Parse command-line arguments """
    parser = ArgumentParser()
    parser.add_argument("csv", help="the path to the csv file")
    parser.add_argument("film", help="the type of film you want to find")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movie_database(args.csv, args.film)