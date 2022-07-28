import pickle
import os 

movie_list = 'movielist.pickle'

movies = []

if os.path.exists(movie_list):
    with open(movie_list,'rb') as rfp:
        movies = pickle.load(rfp)

while True:
    x = input('What would you like to do? Type "watch" to have a movie randomly selected  for you, type "add" to add a movie to your catalog, type "remove" to remove a movie, type "display" to see the current list of movies in your catalog or type "q" to quit.' )

    if x == "add":
        add = input('Add a movie you would like to watch in the following format: Title (Director, Year) then press Enter to add the movie to the list.' )
        movies.append(add)

    if x == "watch":
        import random
        print("Here is your randomly selected movie for Cinema Night!", random.choice(movies))

    if x == "remove":
        r = input('Enter the movie you would like to remove from the catalog using the following format: Title (Director, Year) then press Enter to remove the movie from the catalog.' )
        movies.remove(r)

    if x == "display":
        print("Here is your current catalog of movies to watch: ",*movies, sep = "\n")

    if x == "q":
        break

#open database
with open(movie_list, 'wb') as wfp:
    pickle.dump(movies, wfp)

#update database with changes
with open(movie_list, 'rb') as rfp:
    movies = pickle.load(rfp)

