import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth 
import json
import getenv


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
client_url = os.getenv("REDIRECT_URI")

scope = 'playlist-modify-public'
username = '31y2c7q5lvnkocv6vldslrxqq4ki'
myClientId= client_id
mySecret=client_secret
myRedirect=redirect_uri
token = SpotifyOAuth(scope= scope ,username = username, client_id=myClientId,client_secret= mySecret,redirect_uri= myRedirect)

spotifyobj  = spotipy.Spotify(auth_manager= token)

playlist_name = "base"
playlist_description = "base"


def create_playlist(username,playlist_name,playlist_description):
	return spotifyobj.user_playlist_create(user = username,name= playlist_name,description= playlist_description,public = True)

def artist_uri():
	name = input("enter singer name")
	artist =spotifyobj.search(q=name,limit=1,type='artist')
	artist = artist['artists']['items'][0]['uri']
	return artist

def song_uri():
	user_input = input("enter song name :")
	result= spotifyobj.search(q=user_input,limit = 1,type='track')
	result= result['tracks']['items'][0]['uri']
	songs=[]
	songs.append(result)
	return songs

def add_song(username,song):
	playlist = spotifyobj.user_playlists(user = username)
	play_list = playlist['items']
	playlist_id = play_list[0]['id']
	spotifyobj.user_playlist_add_tracks(user= username,playlist_id=playlist_id,tracks= song)

def get_top_tracks(artist_uri):
	result = spotifyobj.get_top_tracks(artist_uri)
	return result['tracks'][0]['name']


# song_uri= search_uri()
# add_song(username,song_uri)
# print(artist_id())
# print(get_top_tracks(uri))
uri = artist_uri()
song=song_uri()
add_song(username,song)

print(" ")