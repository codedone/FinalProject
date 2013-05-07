import urllib, cStringIO
from PIL import Image, ImageTk
from Tkinter import Tk, Text, Label, Message, Entry, Button, RIGHT, LEFT, BOTH, RAISED, TOP, BOTTOM, X, Y, W
from ttk import Frame, Style
import webbrowser as web
import Search
import reddituserpass


class GUI(Frame):
	
	posts = []
	credentials = []
	
	def __init__(self, parent, _posts):
		Frame.__init__(self, parent)
		
		self.posts = _posts
		
		self.parent = parent
		self.parent.title("Media Portal")
		
		self.initUI()

	def initUI(self):
		
		self.pack(fill=BOTH, expand=1)
		
		#create special frame for buttons at the top
		frame = Frame(self)
		frame.pack(fill=X)
		
		search = Entry(frame)
		
		def callback():
			#create new window
			main(Search.SearchFrontPage(search.get()))
		
		b = Button(frame, text="Search", width=5, command=callback)
		b.pack(side=RIGHT)
		search.pack(side=RIGHT)
		
		def login():
			#change login credentials
			self.credentials = reddituserpass.main()
			self.parent.destroy()
		
		login = Button(frame, text="Login", width=5, command=login)
		login.pack(side=LEFT)
		
		self.drawWindow()

	def drawWindow(self):
		#cache the images to display
		self.redditraw = Image.open("reddit.png").resize((40,40), Image.ANTIALIAS)
		self.redditimg = ImageTk.PhotoImage(self.redditraw)
		
		self.twitterraw = Image.open("twitter.png").resize((40,40), Image.ANTIALIAS)
		self.twitterimg = ImageTk.PhotoImage(self.twitterraw)
		
		for post in self.posts:
			frame = Frame(self)
			frame.pack(side=TOP, fill=X)
			
			#this was for using web images
			#file = cStringIO.StringIO(urllib.urlopen("location").read())
			
			#draw 
			if post.type == "RedditPost":
				reddit = Label(frame, image=self.redditimg)
				reddit.image = self.redditimg
				#reddit.bind("<1>", lambda event, url=post[1]: web.open_new(url))
				reddit.pack(side=LEFT)
			else:
				twitter = Label(frame, image=self.twitterimg)
				twitter.image = self.twitterimg
				#twitter.bind("<1>", lambda event, url=post[1]: web.open_new(url))
				twitter.pack(side=LEFT)
			
			body = Frame(frame)
			body.pack(fill=BOTH)
			
			#the actual post body
			title = Message(body, text=post.title, foreground="#0000dd", justify=LEFT, width=550)
			#title.bind("<1>", lambda event, url=post[4]: web.open_new(url))
			title.pack(anchor=W)
			
			#date and author
			details = Label(body, text=post.date+" by "+post.user)
			details.pack(anchor=W)


def main(posts = Search.FrontPage()):
	
	#main window
	root = Tk()
	root.geometry("600x300+300+300")
	app = GUI(root,posts)
	root.mainloop()

if __name__ == '__main__':
	main()
