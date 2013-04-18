class Post:
    title = ""
    user = ""
    date = ""
    def __init__(self, _title, _user, _date):
        self.title = _title
        self.date = _date
        self.user = _user
    def getTitle():
        return title
    def getUser():
        return user
    def getDate():
        return date

class TwitterPost(Post):
    retweets = 0
    def __init__(self, _title, _user, _date, _retweets):
        self.retweets = _retweets
        return super().__init__(_title, _user, _date)

class RedditPost(Post):
    upvotes = 0
    downvotes = 0
    def __init__(self, _title, _user, _date, _upvotes, _downvotes):
        self.upvotes = _upvotes
        self.downvotes = _downvotes
        return super().__init__(_title, _user, _date)