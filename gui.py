import urllib, cStringIO
from PIL import Image, ImageTk
from Tkinter import Tk, Text, Label, Entry, Button, RIGHT, LEFT, BOTH, RAISED, TOP, BOTTOM, X, Y, W
from ttk import Frame, Style
import webbrowser as web
import Search

class GUI(Frame):
	
	search = Entry()

	def __init__(self, parent):
		Frame.__init__(self, parent)
		
		self.parent = parent
		self.parent.title("Media Portal")
		
		self.initUI()

	def initUI(self):
		
		self.pack(fill=BOTH, expand=1)
		
		search = Entry(self)
		
		def callback():
			print search.get()

		b = Button(self, text="Search", width=5, command=callback)
		b.pack(anchor=W)
		search.pack(anchor=W)
		
		posts = Search.FrontPage()
		
		for post in posts:
			frame = Frame(self)
			frame.pack(side=TOP, fill=X)
			
			#file = cStringIO.StringIO(urllib.urlopen("location").read())
			if post.type == "RedditPost":
				raw = Image.open("reddit.png").resize((40,40), Image.ANTIALIAS)
			else:
				raw = Image.open("twitter.png").resize((40,40), Image.ANTIALIAS)
			img = ImageTk.PhotoImage(raw)
			thumb = Label(frame, image=img)
			thumb.image = img
			#thumb.bind("<1>", lambda event, url=post[1]: web.open_new(url))
			thumb.pack(side=LEFT)
			
			body = Frame(frame)
			body.pack(fill=BOTH)
			
			title = Label(body, text=post.title, foreground="#0000dd")
			#title.bind("<1>", lambda event, url=post[4]: web.open_new(url))
			title.pack(anchor=W)
			
			details = Label(body, text=post.date+" by "+post.user)
			details.pack(anchor=W)


def main():
	
	root = Tk()
	root.geometry("600x300+300+300")
	app = GUI(root)
	root.mainloop()

if __name__ == '__main__':
	main()
