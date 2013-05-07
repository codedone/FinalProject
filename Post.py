class Post(object):
    title = ""
    user = ""
    date = ""
    type = ""
    def __init__(self, _title, _user, _date, _type):
        self.title = _title
        self.date = _date
        self.user = _user
        self.type = _type
    def getTitle():
        return title
    def getUser():
        return user
    def getDate():
        return date

class TwitterPost(Post):
    retweets = 0
    def __init__(self, _title, _user, _date):
        super(TwitterPost, self).__init__(_title, _user, _date, "TwitterPost")

class RedditPost(Post):
    upvotes = 0
    downvotes = 0
    imgURL = ''
    def __init__(self, _title, _user, _date, _upvotes, _downvotes, _URL):
        self.upvotes = _upvotes
        self.downvotes = _downvotes
        self.imgURL = _URL
        super(RedditPost, self).__init__(_title, _user, _date, "RedditPost")