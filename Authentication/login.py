# Fiji Marcelin
# computingID:fm4cg
import tweepy

def loginFunction():
    userBotKey = "insert bot key"
    userSecretKey = "insert secret key"
    sessionAccessToken = ""
    sessionSecretToken = ""
    authenticate = tweepy.OAuthHandler(userBotKey,userSecretKey)
    authenticate.set_access_token(sessionAccessToken,sessionSecretToken)

    return authenticate

