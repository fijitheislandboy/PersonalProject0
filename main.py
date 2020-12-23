# Fiji Marcelin
# computingID:fm4cg
import Authentication.login,tweepy, Status.MakeStatus
import Logging.loggerCode

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

Status.MakeStatus.makePost(callTweepy)