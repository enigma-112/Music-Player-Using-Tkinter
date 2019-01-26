from tkinter import *		#importing tkinter
from pygame import mixer	#importing mixer from pygame
import tkinter.messagebox   # importing the messagebox to show messages
from tkinter import filedialog #importing filedialog to open files






root = Tk()					#intializing the tkinter window

menubar = Menu(root)
root.config(menu = menubar)

subMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=subMenu)

def browse_file():
	global filename
	filename = filedialog.askopenfilename()

subMenu.add_command(label="Open",command=browse_file)
subMenu.add_command(label="Exit")


def about_player():
	tkinter.messagebox.showinfo("Get the code ", "from : https://github.com/enigma-112/Music-Player-Using-Tkinter")



subMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About",command=about_player)










mixer.init() 				#initializing the mixer
root.geometry("400x400")
root.title("Galactic Music Player")
#root.iconbitmap('@m_player.xbm')	
if ( sys.platform.startswith('win')):  		 # loading the icon photo for windows
	root.iconbitmap('m_player.ico')
else:
	logo = PhotoImage(file='m_player.gif')   # loading the icon photo for linux ( in my case it is ubuntu)
	root.call('wm', 'iconphoto', root._w, logo)


textlabel = Label(root,text = "Ambition is my drug, Success is the only cure")
textlabel.pack()

def play():				# defining play function
	mixer.music.load(filename)
	mixer.music.play()


playPhoto = PhotoImage(file="play.png")
playBtn = Button(root,image=playPhoto,command=play)
playBtn.pack()

def stop():              #defining stop function
	mixer.music.stop()

stopPhoto = PhotoImage(file="stop.png")
stopBtn = Button(root,image=stopPhoto,command=stop)
stopBtn.pack()

def volume(val):		# defining volume function
	volume_value= int(val)/100
	mixer.music.set_volume(volume_value) # set_volume takes value from 0 to 1

scale = Scale(root,from_=0, to=100,orient=HORIZONTAL,command=volume )
scale.set(40)  # setting default volume
mixer.music.set_volume(0.4)
scale.pack()








root.mainloop()