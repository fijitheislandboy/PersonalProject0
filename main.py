# Fiji Marcelin
# computingID:fm4cg
import Authentication.login,tweepy, Status.MakeStatus
import logging

logEvents = logging.getLogger()
login = Authentication.login.loginFunction()
callTweepy = tweepy.API(login)

try:
    callTweepy.verify_credentials()
    print("Authentication OK")
except:
    print("Auth problem")

Status.MakeStatus.makePost(callTweepy)