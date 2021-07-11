import requests

TMDB_API= 'cbae2017c8f36c7842741ae80f01a51f'
TMDB_SEARCH_URL= 'https://api.themoviedb.org/3/search/movie'
TMDB_MOVIE_DETAILS_URL= 'https://api.themoviedb.org/3/movie'
TMDB_MOVIE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


movie_id= '577922'
movie_data= requests.get(url=f"{TMDB_MOVIE_DETAILS_URL}/{movie_id}", params={"api_key":TMDB_API}).json()
print(movie_data)