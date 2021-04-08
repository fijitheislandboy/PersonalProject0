import spotipy,os
from spotipy.oauth2 import SpotifyClientCredentials
#import Logging.loggerCode
#this should get the song
#SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
#SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
def spotifyFunction():
    print("hi")
    authenticate = SpotifyClientCredentials()
    starchild = spotipy.Spotify(auth_manager=authenticate)
    print('reach')
    #get the playlist
    myPlaylist = starchild.playlist('0NlZyeckr2Y3vJsotqydub')
    playlistTracks = myPlaylist['tracks']
    songs = playlistTracks['items']
    i = 0
    while playlistTracks['next']:
        playlistTracks = starchild.next(playlistTracks)
        for item in playlistTracks['items']:
            songs.append(item)
        #songs.extend(myPlaylist['items'])

    for song in songs:
        print(song['track']['name'])
    return 0
