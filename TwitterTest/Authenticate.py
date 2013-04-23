
import sys
import os
import string
from twitter import *

def getTwitter():
    APP_NAME = "CSCE315 FinalProject"
    CONSUMER_KEY = "laLkGfnAEQZ8OmoCFFBQ"
    CONSUMER_SECRET = "lEVBBe5vUGwFtuZHd4nAkjeoo1HwEsT7cPHKFcpxsU"

    MY_TWITTER_CREDS = os.path.expanduser('oauth_creds')

    if not os.path.exists(MY_TWITTER_CREDS):
        oauth_dance( APP_NAME, CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

    oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
    twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

    return twitter

# idea taken from stack overflow
# stackoverflow.com/questions/1342000/how-to-replace-non-ascii-characters-in-string
def removeNonAscii(s):
    return "".join(i for i in s if ord(i)<128)
