
from Authenticate import *

twitter = getTwitter()
tweets = twitter.statuses.home_timeline()

fileWrite = open('unsorted_tweets.xml', 'w')
for t in tweets:
    fileWrite.write("<tweet>\n\t")
    fileWrite.write("<author>" + t['user']['screen_name'] + "</author>\n\t")
    fileWrite.write("<post>" + t['text'] + "</post>\n")
    fileWrite.write("</tweet>\n")
