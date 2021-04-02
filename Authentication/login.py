# Fiji Marcelin
# computingID:fm4cg
import tweepy,os, spotipy
import Logging.loggerCode
from spotipy.oauth2 import SpotifyClientCredentials

BOT_KEY = os.environ['BOT_KEY']
USER_SECRET = os.environ['USER_SECRET']
SESSION_TOKEN = os.environ['SESSION_TOKEN']
SESSION_SECRET = os.environ['SESSION_SECRET']

def loginFunction():
    authenticate = tweepy.OAuthHandler(BOT_KEY,USER_SECRET)
    authenticate.set_access_token(SESSION_TOKEN,SESSION_SECRET)
    #change/improve later
    Logging.loggerCode.updateLog("Bot logged in")
    return authenticate

