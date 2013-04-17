
from Authenticate import *

if len(sys.argv) is not 2:
    print("Please post your status as a string in quotes.")
    exit()

statusUpdate = sys.argv[1]

twitter = getTwitter()

twitter.statuses.update(status = statusUpdate)
