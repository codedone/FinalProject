

from Authenticate import *

twitter = getTwitter()
tweets = twitter.statuses.home_timeline()

fileWrite = open('unsorted_tweets.xml', 'w')
for t in tweets:
    userName = t['user']['screen_name']
    post = t['text']

    userName = removeNonAscii(userName)
    post = removeNonAscii(post)

    fileWrite.write("<tweet>\n\t")
    fileWrite.write("<author>" + userName + "</author>\n\t")
    fileWrite.write("<post>" + post + "</post>\n")
    fileWrite.write("</tweet>\n")

fileWrite.close()
