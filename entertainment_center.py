from media import Movie, fetchMovieData
from fresh_tomatoes import open_movies_page

# Empty list of movies
movies = []

# Create movie instances (containing title, poster url, trailer url) from id
ratatouille = fetchMovieData(2062)
movies.append(ratatouille)

the_circle = fetchMovieData(339988)
movies.append(the_circle)

la_la_land = fetchMovieData(313369)
movies.append(la_la_land)

thor_ragnarok = fetchMovieData(284053)
movies.append(thor_ragnarok)

beauty_beast = fetchMovieData(321612)
movies.append(beauty_beast)

fast_five = fetchMovieData(51497)
movies.append(fast_five)

# Send movie data for display
open_movies_page(movies)
