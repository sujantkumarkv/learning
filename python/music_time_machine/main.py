#module imports
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL= 'https://www.billboard.com/charts/hot-100' 
SPOTIFY_CLIENT_ID= '4e63e7789ff64302b71512a74e948ea0'
SPOTIFY_CLIENT_SECRET= '22a50e5dc29e4930b150a58a5c2e70a5'
REDIRECT_URI= 'https://example.com'


time= input('Enter the time in YYYY-MM-DD format of which music U wanna listen.\n')
#print(type(time)) - Its <'str'>
response= requests.get(url= f'{BILLBOARD_URL}/{time}')
billboard_webpage= response.text
''' SCRAPING BILLBOARD SITE FOR DATA''' 
soup= BeautifulSoup(billboard_webpage, 'html.parser')

#print(soup.find(name='span', class_='chart-element__information__song text--truncate color--primary').getText())

songs= []
song_tags= soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')

for song_tag in song_tags:
    song_name= song_tag.getText()
    songs.append(song_name)
    
#print(songs)

#********* CREATING SPOTIPY's OBJECT WITH REQUIRED PARAMETERS PASSED ***********************

sp= spotipy.Spotify(
    auth_manager= SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI, scope='playlist-modify-private',
        cache_path='token.txt', show_dialog=True,
    )
)

#print(sp.current_user()) 
''' Returns this :
{'display_name': 'sujant', 'external_urls': {'spotify': 'https://open.spotify.com/user/8bvo79hvitozk2pfyg1urkszt'}, 'followers': {'href': None, 'total': 0}, 
'href': 'https://api.spotify.com/v1/users/8bvo79hvitozk2pfyg1urkszt', 'id': '8bvo79hvitozk2pfyg1urkszt', 'images': [{'height': None, 'url': 'https://i.scdn.co/image/ab6775700000ee857ac968732ab29108dcf1dff0', 'width': None}], 'type': 'user', 'uri': 'spotify:user:8bvo79hvitozk2pfyg1urkszt'}
'''

user_id= sp.current_user()['id']
songs_uris= []

#***************************   GETTING THE URIs of our 100 tracks   ******************************

year= time.split('-')[0]

for song in songs:
    search_result = sp.search(q=f"track:{song}", type="track")
    
    try:
        uri = search_result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f'{song} not found in spotifys database, sorry !!')


#************************    CREATING A PLAYLIST & THEN ADDING SONGS to it **************************


playlist_creation= sp.user_playlist_create(user=user_id, 
                                           name=f"{time} Billboard 100", 
                                           public=False,
                                            description='Made under music_time_machine python project. \
                                            Contains the top 100 Billboard songs of time you enter,\
                                            here, my bday time :)')


#print(playlist_creation)

sp.playlist_add_items(playlist_id=playlist_creation['id'], 
                      items=songs_uris)


''' ###################### BOOM DONE !!!!!  #######################'''
