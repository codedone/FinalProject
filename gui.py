import urllib, cStringIO
from PIL import Image, ImageTk
from Tkinter import Tk, Text, Label, RIGHT, LEFT, BOTH, RAISED, TOP, BOTTOM, X, Y, W
from ttk import Frame, Style
import webbrowser as web

class GUI(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)
		
		self.parent = parent
		self.parent.title("Media Portal")
		
		self.initUI()

	def initUI(self):
		
		self.pack(fill=BOTH, expand=1)
		
		posts = [["Reddit", "http://upload.wikimedia.org/wikipedia/en/a/af/Maine_Moose_Logo.png", "DrPresley", "Way funnier than the movie!", "http://www.youtube.com/watch?v=LJQ-LZYAMBQ", "today"], \
				 ["Reddit", "http://upload.wikimedia.org/wikipedia/en/a/af/Maine_Moose_Logo.png", "NotACat", "there's a reason it's called the best twitter bot", "https://twitter.com/Horse_ebooks", "today"], \
				 ["Reddit", "http://upload.wikimedia.org/wikipedia/en/a/af/Maine_Moose_Logo.png", "very helpful if you know what you are doing...", "http://www.reddit.com/r/Python/", "yesterday"]]
		
		for post in posts:
			frame = Frame(self)
			frame.pack(side=TOP, fill=X)
			
			file = cStringIO.StringIO(urllib.urlopen(post[1]).read())
			raw = Image.open(file)
			img = ImageTk.PhotoImage(raw)
			thumb = Label(frame, image=img)
			thumb.image = img
			thumb.bind("<1>", lambda event, url=post[1]: web.open_new(url))
			thumb.pack(side=LEFT)
			
			body = Frame(frame)
			body.pack(fill=BOTH)
			
			title = Label(body, text=post[3], foreground="#0000dd")
			title.bind("<1>", lambda event, url=post[4]: web.open_new(url))
			title.pack(anchor=W)
			
			details = Label(body, text=post[5]+" by "+post[2])
			details.pack(anchor=W)


def main():
	
	root = Tk()
	root.geometry("600x300+300+300")
	app = GUI(root)
	root.mainloop()

if __name__ == '__main__':
	main()
