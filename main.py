# Fiji Marcelin
# computingID:fm4cg
import Authentication.login,tweepy, Status.MakeStatus,spotipy
import Logging.loggerCode
import QueryLogic.QueryHandler
querySystem = QueryLogic.QueryHandler
querySystem.spotifyFunction()
logEvents = Logging.loggerCode
login = Authentication.login.loginFunction()
callTweepy = tweepy.API(login)

try:
    callTweepy.verify_credentials()
    print("Authentication OK")
    logEvents.updateLog("Authentication was valid")
except:
    print("Auth problem")
    logEvents.updateLog("Authentication Error")
###################
Status.MakeStatus.makePost(callTweepy)
