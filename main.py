# Fiji Marcelin
# computingID:fm4cg
import Authentication.login,tweepy,Status

login = Authentication.login.loginFunction()
callTweepy = tweepy.API(login)

try:
    callTweepy.verify_credentials()
    print("Authentication OK")
except:
    print("Auth problem")


