
from Login import *
from GetSubreddit import *

client = login('CodedOne', 'squidharder9976')
j = subredditInfo(client, limit=100)

fileWrite = open('unsorted_posts.xml', 'w')
for story in j:
    username = story['data']['author']
    post = story['data']['title']
    url = story['data']['url']

    if not story['data']['over_18']:
        fileWrite.write("<post>\n\t")
        fileWrite.write("<author>" + username + "</author>\n\t")
        fileWrite.write("<title>" + post + "</title>\n\t")
        fileWrite.write("<url>" + url + "</url>\n")
        fileWrite.write("</post>\n")

fileWrite.close()
