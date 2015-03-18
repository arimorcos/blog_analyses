__author__ = 'arimorcos'

import datetime
import sys
sys.path.extend(['D:\\Documents\\GitHub\\getRedditDataset', 'D:\\Documents\\GitHub\\reddit_analyses'])
from redditDataset import *

if __name__ == '__main__':

    shouldOneHour = False

    # handle arguments
    startDate = sys.argv[1]
    endDate = sys.argv[2]
    dbName = sys.argv[3]
    fineScale = int(sys.argv[4])
    shouldOneHour = bool(sys.argv[5])
    offset = int(sys.argv[6])

    newDefaults = ['art', 'askscience', 'blog', 'creepy', 'dataisbeautiful', 'DIY', 'Documentaries', 'fitness',
                   'food', 'futurology', 'gadgets', 'getmotivated', 'history', 'internetisbeautiful', 'jokes',
                   'lifeprotips', 'listentothis', 'mildlyinteresting', 'nosleep', 'nottheonion', 'oldschoolcool',
                   'personalfinance', 'philosophy', 'photoshopbattles', 'showerthoughts', 'space', 'sports', 'tifu',
                   'twoxchromosomes', 'upliftingnews', 'writingprompts']

    r = praw.Reddit(user_agent='grab_defaults')
    sub = list(getSubreddits(r, newDefaults))
    if shouldOneHour:
        hour = 9
        # get number of days between dates
        startDay = datetime.date(2000 + int(startDate[0:2]), int(startDate[2:4]), int(startDate[4:6]))
        endDay = datetime.date(2000 + int(endDate[0:2]), int(endDate[2:4]), int(endDate[4:6]))
        nDays = (endDay - startDay).days

        # loop through each day and create dataset
        for day in range(offset,nDays):
            # get temp start and stop
            tempStartObj = datetime.datetime(2000 + int(startDate[0:2]), int(startDate[2:4]), int(startDate[4:6]),
                                             hour, int(startDate[8:10]), int(startDate[10:12]))
            tempStartObj = tempStartObj + datetime.timedelta(days=day)
            tempStopObj = tempStartObj + datetime.timedelta(hours=2)

            # convert to strings
            tempStartStr = tempStartObj.strftime('%y%m%d%H%M%S')
            tempStopStr = tempStopObj.strftime('%y%m%d%H%M%S')

            # create dataset
            createDataset(r, sub, startDate=tempStartStr, endDate=tempStopStr, dbName=dbName + '_day_' + str(day).zfill(3),
                          fineScale=fineScale)
    else:
        createDataset(r, sub, startDate=startDate, endDate=endDate, dbName=dbName, fineScale=fineScale)
