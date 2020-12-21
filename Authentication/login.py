# Fiji Marcelin
# computingID:fm4cg
import tweepy
def loginFunction():
    userBotKey = "insert bot key"
    userSecretKey = "insert secret key"
    authenticate = tweepy.OAuthHandler(userBotKey,userSecretKey)
    return authenticate

