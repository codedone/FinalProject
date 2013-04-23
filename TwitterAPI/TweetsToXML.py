

from Authenticate import *

twitter = getTwitter()
tweets = twitter.statuses.home_timeline()

fileWrite = open('unsorted_tweets.xml', 'w')
for t in tweets:
    userName = t['user']['screen_name']
    post = t['text']
    date = t['created_at']

    # get only date from created_at
    splitDate = date.split(' ')
    # below is hardcoded for Twitter's created_at format
    date = splitDate[1] + " " + splitDate[2] + " " + splitDate[-1]

    userName = removeNonAscii(userName)
    post = removeNonAscii(post)

    fileWrite.write("<tweet>\n\t")
    fileWrite.write("<author>" + userName + "</author>\n\t")
    fileWrite.write("<post>" + post + "</post>\n\t")
    fileWrite.write("<date>" + date + "</date>\n")
    fileWrite.write("</tweet>\n")

fileWrite.close()
