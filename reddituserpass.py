from Tkinter import *


class Login(Frame):
	
	data = []
	
	def __init__(self, parent):
		Frame.__init__(self, parent)
		
		self.parent = parent
		self.parent.title("Login")
		
		self.initUI()

	def initUI(self):
		self.pack(fill=BOTH, expand=1)
		
		def makeentry(parent, caption, width=None, **options):
			frame = Frame(parent)
			Label(frame, text=caption).pack(side=LEFT)
			entry = Entry(frame, **options)
			if width:
				entry.config(width=width)
			entry.pack(side=LEFT)
			frame.pack(fill=X)
			return entry

		user = makeentry(self, "User name:", 10)
		password = makeentry(self, "Password:", 10, show="*")

		def callback():
			self.data = [user.get(), password.get()]
			self.parent.destroy()

		b = Button(self, text="Login", width=10, command=callback)
		b.pack()

def main():
	root = Tk()
	app = Login(root)
	root.mainloop()
	return app.data

if __name__ == '__main__':
	main()

