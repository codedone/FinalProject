import Post
import string
import re
import random
import PostsToXML

def InitializeRedditFromXML():
    redditList = []

    post = ''
    user = ''
    date = '1/1/2013'
    URL = ''

    PostsToXML #update XML to retrieve latest posts
    f = open('RedditAPI/unsorted_posts.xml') #open file for reading

    for line in f: 
        line = ' '.join(line.split())
        if line == '<post>': #break out XML file based on tag
            continue
        if '<author>' in line:
            user = line
            user = user.replace('<author>','').replace('</author>','')
        if '<title>' in line:
            post = line
            post = post.replace('<title>','').replace('</title>','')
        if '<url>' in line:
            URL = line
            URL = URL.replace('<url>','').replace('</url>','')
        if line == '</post>':
            p = Post.RedditPost(post, user, date, 0, 0, URL) #take parsed information and create a Post object
            redditList.append(p)
            post = ''
            user = ''
            url = ''

    return redditList

def InitializeTwitterFromXML():
    tweetList = []
    post = ''
    user = ''
    date = '1/1/2013' 

    f = open('TwitterAPI/unsorted_tweets.xml') #open XMl file for reading

    while True:
        line = f.readline()
        if not line: break
        line = ' '.join(line.split())
        if line == '<tweet>':  #parse XML file based on tags
            continue
        if "<post>" in line:
            post+=line
            while "</post>" not in line:
                line = f.readline()
                post+=' '
                post+=line
            post = post.replace("<post>","").replace("</post>","")
        if "<author>" in line:
            user += line
            while "</author>" not in line:
                line = f.readline()
                user += ' '
                user += line
            user = user.replace("<author>","").replace("</author>","")
        if "<date>" in line:
            date = line
            date = date.replace("<date>","").replace("</date>","")
        if line == "</tweet>":
            p = Post.TwitterPost(post,user,date) #create object from parsed data
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
        for word in line: #traverse through all words and find posts that match search parameters
            if param.lower() in word.lower():
                RelevantPosts.append(post)
                break

    for post in RedditList:
        line = post.title.split()
        for word in line: #traverse through all words and find posts that match search parameters
            if param.lower() in word.lower():
                RelevantPosts.append(post)
                break

    random.shuffle(RelevantPosts)

    return RelevantPosts

def FrontPage():
    PostList = InitializeTwitterFromXML()
    PostList2 = InitializeRedditFromXML()

    for post in PostList2: #combines Reddit and Twitter Posts
        PostList.append(post)
    
    random.shuffle(PostList)
    return PostList


