# Movie Trailer Website
Source code for a Movie Trailer website.

*By Manuinder Sekhon*
#
It displays trailers for different movies upon clicking on their poster images. You can also add new movies to the website. See below for instructions.


## Prerequisites
* Signup for free TMdb [API KEY](https://developers.themoviedb.org/3/getting-started/introduction)
* An active internet connection

## Installation

#### Ubuntu

```
$ sudo apt-get update
$ sudo apt-get install python3
```

#### Windows
* Download python install package [here](https://www.python.org/downloads/) and install it.

## Usage

>If on Linux:
* Open terminal. Execute the following commands.

```bash
$ unzip Movie-Trailer-Website.zip
$ cd Movie-Trailer-Website

$ export API_KEY=your_api_key
$ python3 entertainment_center.py
```

>If on Windows:
* Delete the following lines in `media.py`
```python
if not os.environ.get("API_KEY"):
        raise RuntimeError("API_KEY not set")

API_KEY = os.environ.get("API_KEY")
```

* Replace them with
```python
API_KEY = "your_api_key"
```
* Run `entertainment_center.py` in python.


## Add New Movies
Search for movie you want to add in project on TMDb website. Extract id from its url and add the movie in `entertainment_center.py`.

*https://www.themoviedb.org/movie*/**399035**-*the-commuter*


## Contributers
1. [*Udacity*](https://www.udacity.com/) : For providing starter code.
1. [*TMDb*](https://www.themoviedb.org/en) : For providing API
