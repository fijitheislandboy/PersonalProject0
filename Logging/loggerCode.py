import logging
import datetime

startLog = logging.getLogger()
date = datetime.date()
time = datetime.time()
def updateLog(phrase):
    startLog.info("On " + date + "at " + time + phrase)
    return 0