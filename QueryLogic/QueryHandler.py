import spotipy, Logging.loggerCode,os
from spotipy.oauth2 import SpotifyClientCredentials
#this should get the song
SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
def spotifyFunction(username):
    authenticate = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)
    starchild = spotipy.Spotify(auth_manager=authenticate)
    #get the playlist
    myPlaylist = starchild.playlist('0NlZyeckr2Y3vJsotqydub')
    #use data in playlist and generate a random number to determine which song in the
    #playlist to use?
    song = myPlaylist['items']
    while myPlaylist['next']:
        myPlaylist = starchild.next(myPlaylist)
        song.extend(myPlaylist['items'])
    for value in song:
        print(song['name'])
    return 0