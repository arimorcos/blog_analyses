__author__ = 'arimorcos'

import re
import urllib2
import enchant
from textstat.textstat import textstat


def countWords(commentList):
    """
    :param commentList: list of text
    :return: word count
    """

    # get count in each string
    commentCount = [len(commentStr.split()) for commentStr in commentList]

    return sum(commentCount)


def countMisspellings(commentList):
    """
    Count the number of misspelled words
    :param commentList:
    :return: the count of misspelled words
    """

    # create dictionary object
    dictionary = enchant.Dict('en-US')

    # count misspelled words
    misSpelledCount = 0
    for comment in commentList:

        misSpelledCount += sum([not dictionary.check(word) for word in comment.split()])

    return misSpelledCount


def getReadabilityStats(text):

    # get scores
    fleschGrade = textstat.flesch_kincaid_grade(text)

    # store
    return {'fleschGrade': fleschGrade}


def getCelebList():
    """
    Grabs celebrity list from people.com
    :return: list of celebrities
    """
    response = urllib2.urlopen('http://www.people.com/people/celebrities/')
    html = response.read()
    pattern = r"(?<=id\=\"\d{8}\"\>)\w+\s\w+"
    celebList = re.findall(pattern, html)
    return celebList


def findCelebrityMentions(commentList, celebList):
    """
    Find number of mentions of a given celebrity
    :param commentList: list of comments
    :param celebList: list of celebrities
    :return: number of mentions of a given celebrity (only exact spelling)
    """

    # join all comments
    allComments = " ".join(commentList)

    # convert to lower case
    allComments = allComments.lower()

    # find counts of each celebrity
    celebCount = {}
    for celeb in celebList:

        celebCount[celeb] = len(re.findall(celeb.lower(), allComments))

    return celebCount


