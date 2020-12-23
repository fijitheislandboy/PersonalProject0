import tweepy
import Logging.loggerCode
def makePost(apiFunction):
    apiFunction.update_status("hello World")
    statusText = "hello World"
    Logging.loggerCode.updateLog("New status was posted with text" + statusText)
    return 0
