from Tkinter import *

root = Tk()

def makeentry(parent, caption, width=None, **options):
	frame = Frame(parent)
	Label(frame, text=caption).pack(side=LEFT)
	entry = Entry(frame, **options)
	if width:
		entry.config(width=width)
	entry.pack(side=LEFT)
	frame.pack(fill=X)
	return entry

user = makeentry(root, "User name:", 10)
password = makeentry(root, "Password:", 10, show="*")

def callback():
	combo = [user.get(), password.get()]
	print combo

b = Button(root, text="Login", width=10, command=callback)
b.pack()

mainloop()
