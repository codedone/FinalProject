import Post
import string
import re
import random

def InitializeRedditFromXML():
    redditList = []

    post = ''
    user = ''
    date = '1/1/2013'
    URL = ''

    f = open('RedditAPI/unsorted_posts.xml')

    for line in f:
        line = ''.join(line.split())
        if line == '<post>':
            continue
        if '<author>' in line:
            user = line
            user = user.replace('<author>','').replace('</author>','')
        if '<title>' in line:
            post = line
            user = user.replace('<title>','').replace('</title>','')
        if '<url>' in line:
            URL = line
            URL = URL.replace('<url>','').replace('</url>','')
        if line == '</post>':
            p = Post.RedditPost(post, user, date, 0, 0, URL)
            redditList.append(p)
            post = ''
            user = ''
            url = ''

    return redditList

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
        if "<date>" in line:
            date = line
            date = date.replace("<date>","").replace("</date>","")
        if line == "</tweet>":
            p = Post.TwitterPost(post,user,date)
            tweetList.append(p)
            post = ''
            user = ''
            date = '1/1/2001'

    return tweetList

def SearchFrontPage(param):
    TwitterList = InitializeTwitterFromXML()
    RedditList = InitializeRedditFromXML()
    RelevantPosts = []

    for post in TwitterList:
        line = post.title.split()
        for word in line:
            if param.lower() in word.lower():
                RelevantPosts.append(post)
                break

    for post in RedditList:
        line = post.title.split()
        for word in line:
            if param.lower() in word.lower():
                RelevantPosts.append(post)
                break

    random.shuffle(RelevantPosts)

    return RelevantPosts

def FrontPage():
    PostList = InitializeTwitterFromXML()
    PostList2 = InitializeRedditFromXML()

    for post in PostList2:
        PostList.append(post)

    return random.shuffle(PostList)
