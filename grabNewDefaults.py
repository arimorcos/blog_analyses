__author__ = 'arimorcos'

import datetime
from redditDataset import *

if __name__ == '__main__':

    shouldOneHour = False

    # handle arguments
    startDate = sys.argv[1]
    endDate = sys.argv[2]
    dbName = sys.argv[3]
    fineScale = int(sys.argv[4])
    shouldOneHour = bool(sys.argv[5])

    newDefaults = ['art', 'askscience', 'blog', 'creepy', 'dataisbeautiful', 'DIY', 'Documentaries', 'fitness',
                   'food', 'futurology', 'gadgets', 'getmotivated', 'history', 'internetisbeautiful', 'jokes',
                   'lifeprotips', 'listentothis', 'mildlyinteresting', 'nosleep', 'nottheonion', 'oldschoolcool',
                   'personalfinance', 'philosophy', 'photoshopbattles', 'showerthoughts', 'space', 'sports', 'tifu',
                   'twoxchromosomes', 'upliftingnews', 'writingprompts']

    r = praw.Reddit(user_agent='grab_defaults')
    sub = getSubreddits(r, newDefaults)
    if shouldOneHour:
        hour = 9
        # get number of days between dates
        startDay = datetime.date(int(startDate[0:2]), int(startDate[2:4]), int(startDate[4:6]))
        endDay = datetime.date(int(endDate[0:2]), int(endDate[2:4]), int(endDate[4:6]))
        nDays = (endDay - startDay).days

        # loop through each day and create dataset
        for day in range(nDays):
            # get temp start and stop
            tempStartObj = datetime.datetime(int(startDate[0:2]), int(startDate[2:4]), int(startDate[4:6]),
                                             hour, int(startDate[8:10]), int(startDate[10:12]))
            tempStartObj = tempStartObj + datetime.timedelta(days=day)
            tempStopObj = tempStartObj + datetime.timedelta(hours=1)

            # convert to strings
            tempStartStr = tempStartObj.strftime('%y%m%d%H%M%S')
            tempStopStr = tempStopObj.strftime('%y%m%d%H%M%S')

            # create dataset
            createDataset(r, subreddits, startDate=tempStartStr, endDate=tempStopStr, dbName=dbName + '_day_' + str(day),
                          fineScale=fineScale)
    else:
        createDataset(r, subreddits, startDate=startDate, endDate=endDate, dbName=dbName, fineScale=fineScale)
