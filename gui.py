import urllib, cStringIO
from PIL import Image, ImageTk
from Tkinter import Tk, Text, Label, RIGHT, LEFT, BOTH, RAISED, TOP, BOTTOM, X, Y, W
from ttk import Frame, Style
import webbrowser

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
				 ["Reddit", "http://upload.wikimedia.org/wikipedia/en/a/af/Maine_Moose_Logo.png", "SirWilhelm", "very helpful if you know what you are doing...", "http://www.reddit.com/r/Python/", "yesterday"]]
		
		for x in range(0, 3):
			frame = Frame(self)
			frame.pack(side=TOP, fill=X)
			
			file = cStringIO.StringIO(urllib.urlopen(posts[x][1]).read())
			raw = Image.open(file).resize((40,40), Image.ANTIALIAS)
			img = ImageTk.PhotoImage(raw)
			thumb = Label(frame, image=img)
			thumb.image = img
			thumb.bind("<1>", lambda event, index=x: self.click_link(event, index))
			thumb.pack(side=LEFT)
			
			body = Frame(frame)
			body.pack(fill=BOTH)
			
			title = Label(body, text=posts[x][3], foreground="#0000dd")
			title.bind("<1>", lambda event, index=x: webbrowser.open_new(posts[index][4]))
			title.pack(anchor=W)
			
			details = Label(body, text=posts[x][5]+" by "+posts[x][2])
			details.pack(anchor=W)


	def click_link(self, event, index):
		print "you clicked %i" % index

def main():
	
	root = Tk()
	root.geometry("600x300+300+300")
	app = GUI(root)
	root.mainloop()

if __name__ == '__main__':
	main()
