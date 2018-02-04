from media import Movie
from fresh_tomatoes import open_movies_page

# Empty list of movies
movies = []

# Create movie instances (containing title, poster url, trailer url)
# Movie 1
ratatouille = Movie("Ratatouille",
                    "http://www.gstatic.com/tv/thumb/movieposters/165058/p165058_p_v8_aj.jpg",
                    "https://www.youtube.com/watch?v=uVeNEbh3A4U")

# Movie 2
the_circle = Movie("The Circle",
                   "https://upload.wikimedia.org/wikipedia/en/8/80/The_Circle_%282017_film%29.png",
                   "https://www.youtube.com/watch?v=ZkzpcfY9JAo")

# Movie 3
la_la_land = Movie("La La Land",
                   "https://assets.voxcinemas.com/posters/P_HO00004194.jpg",
                   "https://www.youtube.com/watch?v=0pdqf4P9MB8")

# Movie 4
thor_ragnarok = Movie("Thor: Ragnarok",
                      "https://images-na.ssl-images-amazon.com/images/I/A1VBHbAzoKL._RI_SX200_.jpg",
                      "https://www.youtube.com/watch?v=ue80QwXMRHg")

# Movie 5
beauty_beast = Movie("Beauty and the Beast",
                     "https://i.ytimg.com/vi/g-DkY-drN9Q/movieposter.jpg",
                     "https://www.youtube.com/watch?v=e3Nl_TCQXuw")

# Movie 6
fast_five = Movie("Fast Five",
                  "https://images.susu.org/unionfilms/films/posters/xlarge/fast-five.jpg",
                  "https://www.youtube.com/watch?v=vcn2GOuZCKI")

# Append movies to list
movies = [ratatouille, the_circle, la_la_land, thor_ragnarok, beauty_beast, fast_five]

# Send movie data for display
open_movies_page(movies)
