# Final-Project
 
.gitignore:
The .gitignore file is the initial commit of our groups repository.
 
 
FINAL-PROJECT.py:
FINAL-PROJECT.py is the python file containing our code for the decade movie generator. It consists of eight different methods that work together to return different types of movies based on how the user responds to the prompts. The program will ask what decade the they want to view movies from, as well as what type of movie the user wants to see (i.e. documentaries, regular movies etc.). Before the user gets to the generator, our code will ask for the user's age in order to verify that the user is old enough to access the databse without a parent. If the user’s answers with an age below 13, the program will terminate. This is due to an age restriction to use our generator, since some of the movies in the database may not be suitable for younger users. If the user enters an age greater than or equal to 13, the program will then move on.
 
movies.csv:
movies.csv is the text file containing all the movies that the generator will search through. In total, the text file possesses 114 different movies. Each line is a new movie with all of its corresponding information. The first part of each line is the title of the video, followed by what kind of movie it is (whether it is a regular movie or a documentary, etc.), the director, the films rating (on a scale of one to ten), its runtime (in minutes), the year the film was released, and lastly the genre. All information present in this file is accurate as per IMDb.
 
 
README.md:
The README.md file includes our groups documentations, including an explanation of the purpose of each file within the repository, instructions on how to run the movie generator from the command line, as well as how to interpret the output, and an example output. Finally, an annotated bibliography of the sources the group used to develop the generator is also present.
 
test1.py:
test1.py is the test script for our movie generator’s “parse args” function.
To run this test use the command: pytest test1.py -s
 
test2.py:
test2.py is the test script for our movie generator’s init(), and print_movies() function.
To run this test use the command: pytest test2.py -s
 
test3.py:
test3.py is the test script for our movie generator’s “age_verification” function.
To run this test use the command: pytest test3.py -s
 
 
CODE INSTRUCTIONS:
In order to run the program from the command line, use the following command:
python3 FINAL_PROJECT.py movies.csv
Note: For Windows users substitute python3 for python.
From here, respond to the prompts as outlined below.
The program will first ask the user what their age is. Type your age next to the prompt as an integer. (EXAMPLE: type "16", "23", "46", NOT “twenty six” or “thirty-two”) make sure there are no spaces between the numbers and that you enter an integer greater than 0.
If the users age is less than 13, the program will return a message informing the user that they are too young to access the databse without their
parents permission.
If the users age is greater than 13, it will continue to the next prompt.
Next, the program will ask the user what decade they want to see movies from. Type the desired decade as an integer. (EXAMPLE: If you want to see movies from the 1960’s, type "1960" next the prompt. DO NOT type “1960’s” or nineteen sixties.)
DO NOT input any decades that took place after the 2010’s or before the 1950’s as the movie file does not have movies from those years.
DO NOT type in a specific year. For example, if you want to see a movie from 1998, type in "1990" in the command line and then look for movies from 1998 in the dataframe that is generated.
Once the user is done has selected their desired decade, the command line will ask the user what type of film they want to see. Respond with one of the following choices: Movie, Documentary, TV-S (TV series), TV-M (movies), Short.
Note: This will not display those film's from your previously selected decade. This function will return ALL the films in the database that match your selection.
By answering "Movie", the generator will return the movies the movies.csv file contains
By answering "Documentary", the generator will return the documentaries the movies.csv file contains
By answering "TV-S", the generator will return the TV series the movies.csv file contains
By answering "TV-M", the generator will return the TV movies the movies.csv file contains
By answering "Short", the generator will return the short films the movies.csv file contains
 
 
INTERPRETING THE OUTPUT OF THE PROGRAM:
The program first welcomes the user and explains what the purpose of the program is. This information is printed out as part of the opening function.
Our Movie Generator will then prompt the user for their age. If their age is greater than 13, then the user will be able to continue using the program. However, if the user's age is less than 13, the generator will return the message: “The age of {age} is to young. You'll need a parents approval to access movies in this database!” and terminate the program.
Once the user's age is verified, the program will print the first five and last five movies in the database. Please note this does not display every movie in the file, just the first few and last few.
The program will then prompt the user for a decade they want to see movies from. The user has the option of choosing decades between and including the 1950’s through to the 2010’s. The resulting dataframe will display ALL the movies in the file that were released in the decade chosen by the user. The corresponding information includes the title of the movie, followed by what type of film it is, the director, the rating, the runtime, the year it was released, and the genre of the movie.
After the program returns the movies filtered by decade, it will then prompt the user for the type of film they want to see. Type of film refers to the type of film the user wants to view. The options are: Movie, Documentary, TV-S (TV series), TV-M (TV moviess) and Short (short films). When the user types their choice in the command line, the program will return the films that match the request of the user, as well as all the films corresponding information.
 
EXAMPLE OUTPUT:
If the user enters an age greater than or equal to 13, the following dataframe should be displayed:
                 title filmtype            director  rating  duration  year       genre
0                 11:14    Movie         Greg Marcks     7.2      86.0  2003       Crime
1                    42    Movie     Brian Helgeland     7.5     128.0  2013  Biography
2                   300    Movie         Zack Snyder     7.7     117.0  2006     Action
3                   360    Movie  Fernando Meirelles     5.9     110.0  2011      Drama
4                  1408    Movie     Mikael Håfström     6.7     104.0  2007     Horror
..                  ...      ...                 ...     ...       ...   ...         ...
109      A Touch of Sin    Movie         Zhangke Jia     7.2     133.0  2013       Drama
110      A Touch of Zen    Movie             King Hu     7.5     200.0  1971   Adventure
111  A Trip to the Moon    Short      Georges Méliès     8.2      13.0  1902   Adventure
112    A View to a Kill    Movie           John Glen     6.3     131.0  1985      Action
113       A World Apart    Movie        Chris Menges     6.8     112.0  1988       Drama
 
The user will then be prompted to enter a decade that they would like to view films from". If the user enters "1980" the following dataframe should be displayed:
                                                title filmtype          director  rating  duration  year                     genre
11                             *batteries not included    Movie   Matthew Robbins     6.3     106.0  1987             Drama/Sci-Fi
29                      2010: The Year We Make Contact    Movie       Peter Hyams     6.8     116.0  1984                    Sci-Fi
34                              3 Hommes Et Un Couffin    Movie    Coline Serreau     6.4     106.0  1985                    Comedy
58                               A Chinese Ghost Story    Movie    Siu-Tung Ching     7.4      98.0  1987  Comedy/Romance/Thriller
59                                   A Christmas Story    Movie         Bob Clark     8.0      94.0  1983             Comedy/Family
60                                   A City of Sadness    Movie   Hsiao-hsien Hou     7.7     157.0  1989                     Drama
65                                  A Dry White Season    Movie      Euzhan Palcy     6.8     107.0  1989    Drama/History/Thriller
66                                 A Fish Called Wanda    Movie  Charles Crichton     7.6     108.0  1988              Comedy/Crime
85                           A Nightmare on Elm Street    Movie        Wes Craven     7.5      91.0  1984                    Horror
86   A Nightmare on Elm Street Part 2: Freddy's Rev...    Movie      Jack Sholder     5.3      87.0  1985                    Horror
88                                  A Passage to India    Movie        David Lean     7.3     164.0  1984   Adventure/Drama/History
92                              A Question of Silence     Movie    Marleen Gorris     6.6      92.0  1982                     Drama
95                                  A Room with a View    Movie       James Ivory     7.3     117.0  1985                     Drama
112                                   A View to a Kill    Movie         John Glen     6.3     131.0  1985                    Action
 
Next, the user will be prompted for a specific "filmtype". If the user enters "Documentary" the following dataframe should be displayed:
                                  title     filmtype                                director  rating  duration  year                   genre
9                                   45365  Documentary              Bill Ross IV & Turner Ross     6.9      90.0  2009            Documentary
12                               ¡Cuatro!  Documentary                             Tim Wheeler     8.4      75.0  2012             Documentary
13  10 Days Out: Blues from the Backroads  Documentary                     Noble Lincoln Jones     8.0     106.0  2007             Documentary
14                            100 Cameras  Documentary                          Lars von Trier     3.6      15.0  2000            Documentary
27                   20 Feet From Stardom  Documentary                          Morgan Neville     7.8      91.0  2013       Documentary/Music
39                         4 Little Girls  Documentary                               Spike Lee     7.7     102.0  1997     Documentary/History
43                                  49 Up  Documentary             Paul Almond & Michael Apted     7.7     180.0  2005  Documentary/Biography
46                                  56 Up  Documentary                           Michael Apted     7.8     144.0  2012             Documentary
52                  9/11: Ten Years Later  Documentary                            James Hanlon     7.9      60.0  2011             Documentary
53                    A Band Called Death  Documentary  Mark Christopher Covino & Jeff Howlett     7.4      96.0  2012         Biography/Music
56                A Brief History of Time  Documentary                            Errol Morris     7.4      80.0  1991   Documentary/Biography
73                       A Jihad for Love  Documentary                           Parvez Sharma     6.6      81.0  2007             documentary
94                       A Road Not Taken  Documentary        Christina Hemauer & Roman Keller     7.9      66.0  2010             Documentary
 
 
 
Annotated Bibliography:
(2009, January 7). What does if __name__==”___main__”: do? Stack Overflow. https://stackoverflow.com/questions/419163/what-does-if-name-main-do
We used this resource within our repository in order to write our docstring for the if __name__==”___main__” statement at the end of our code. This resource helped us to understand what this function does and how to explain it to our users through the use of docstrings.



