
import sys
import os
from twitter import *

if len(sys.argv) is not 2:
    print("Please post your status as a string in quotes.")
    exit()

statusUpdate = sys.argv[1]

MY_TWITTER_CREDS = os.path.expanduser('oauth_creds')

if not os.path.exists(MY_TWITTER_CREDS):
	oauth_dance("CSCE315 FinalProject", "laLkGfnAEQZ8OmoCFFBQ", "lEVBBe5vUGwFtuZHd4nAkjeoo1HwEsT7cPHKFcpxsU", MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, "laLkGfnAEQZ8OmoCFFBQ", "lEVBBe5vUGwFtuZHd4nAkjeoo1HwEsT7cPHKFcpxsU"))
twitter.statuses.update(status = statusUpdate)

