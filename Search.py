import Post
import string
import re

def InitializeTwitterFromXML():
    tweetList = []
    post = ''
    user = ''
    date = '1/1/2013' #needs to be read in once included in xml

    f = open('unsorted_tweets.xml')

    for line in f:
        line = ''.join(line.split())
        if line == '<tweet>':
            continue
        if "<post>" in line:
            post+=line
            while "</post>" not in line:
                line = f.readline()
                post+=line
            post = post.replace("<post>","").replace("</post>","")
        if "<author>" in line:
            user += line
            while "</author>" not in line:
                line = f.readline()
                user += line
            user = user.replace("<author>","").replace("</author>","")
        if line == "</tweet>":
            p = Post.TwitterPost(post,user,date,0)
            tweetList.append(p)
            post = ''
            user = ''

    return tweetList


def FrontPage():
    PostList = InitializeTwitterFromXML()
    return PostList #this is temporary for Matt to do his UI stuff