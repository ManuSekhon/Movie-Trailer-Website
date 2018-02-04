import urllib.request
import json


class Movie:
    """Implements a movie class"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


def fetchMovieData(movie_id):
    """Gets movie data from TMDB API using movie id"""

    # API key and request url for tmdb
    API_KEY = "346f2929425925b334c2bdeb2331267f"
    request = "https://api.themoviedb.org/3/movie"

    # Also request videos for movie
    video = "append_to_response=videos"

    # Final url to fetch movie data
    url = "{}/{}?api_key={}&{}".format(request, movie_id, API_KEY, video)

    try:
        # Connect to url
        webpage = urllib.request.urlopen(url)

        # Read data from page
        data = webpage.read.decode("utf-8")

        # Convert to JSON for easy parsing
        movie_info = json.loads(data)

        return Movie(movie_info["original_title"],
                     "https://image.tmdb.org/t/p/w500{}".format(movie_info["poster_path"]),
                     "https://www.youtube.com/watch?v={}".format(movie_info["videos"]["results"]["0"]["key"]))

    except:
        return None