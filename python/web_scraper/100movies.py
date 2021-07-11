import requests
from bs4 import BeautifulSoup

URL= 'https://www.empireonline.com/movies/features/best-movies-2'
response= requests.get(url=URL)
webpage_content= response.text

soup= BeautifulSoup(webpage_content, 'html.parser')

movies= soup.find_all(name='h3', class_="jsx-4245974604")
print(movies)

''' OK THIS MUST WORK, THERE'S NO ISSUE WITH CODE but it doesnt work, printing empty list for movies :() '''