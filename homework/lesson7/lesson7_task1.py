# A simple function.

# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. 
# The function should then print "My favorite movie is named {name}".

def favorite_movie(movie):
    print(f"My favorite movie is named {movie}.")

my_movie = input("What is your favorite movie? ")
favorite_movie(my_movie)