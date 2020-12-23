# Fiji Marcelin
# computingID:fm4cg
import tweepy
import Logging.loggerCode


def loginFunction():
    userBotKey = "insert bot key"
    userSecretKey = "insert secret key"
    sessionAccessToken = ""
    sessionSecretToken = ""
    authenticate = tweepy.OAuthHandler(userBotKey,userSecretKey)
    authenticate.set_access_token(sessionAccessToken,sessionSecretToken)
    #change/improve later
    Logging.loggerCode.updateLog("Bot logged in")
    return authenticate

