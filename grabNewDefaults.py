__author__ = 'arimorcos'

import praw
from redditDataset import *

if __name__ == '__main__':

    # handle arguments
    startDate = sys.argv[1]
    endDate = sys.argv[2]
    dbName = sys.argv[3]
    fineScale = int(sys.argv[4])

    newDefaults = ['art', 'askscience', 'blog', 'creepy', 'dataisbeautiful', 'DIY', 'Documentaries', 'fitness',
                   'food', 'futurology', 'gadgets', 'getmotivated', 'history', 'internetisbeautiful', 'jokes',
                   'lifeprotips', 'listentothis', 'mildlyinteresting', 'nosleep', 'nottheonion', 'oldschoolcool',
                   'personalfinance', 'philosophy', 'photoshopbattles', 'showerthoughts', 'space', 'sports', 'tifu',
                   'twoxchromosomes', 'upliftingnews', 'writingprompts']

    r = praw.Reddit(user_agent='grab_defaults')
    sub = getSubreddits(r, newDefaults)
    createDataset(r, subreddits, startDate=startDate, endDate=endDate, dbName=dbName, fineScale=fineScale)
