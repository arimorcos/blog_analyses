__author__ = 'arimorcos'

import re
import urllib2


def countWords(commentList):
    """
    :param commentList: list of text
    :return: word count
    """

    # get count in each string
    commentCount = [len(commentStr.split()) for commentStr in commentList]

    return sum(commentCount)


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


