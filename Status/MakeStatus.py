import tweepy, spotipy
import Logging.loggerCode
def makePost(apiFunction):
    #this is to hold the link returned from spotify
    returnLink = 0
    apiFunction.update_status("hello World! I am Starchild!") #insert link here to update status
    statusText = "hello World! I am Starchild!" #show the text
    Logging.loggerCode.updateLog("New status was posted with text" + statusText)
    return 0
