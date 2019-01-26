from tkinter import *		#importing tkinter
from pygame import mixer	#importing mixer from pygame
root = Tk()					#intializing the tkinter window

mixer.init() 				#initializing the mixer
root.geometry("400x400")
root.title("Galactic Music Player")
#root.iconbitmap('@m_player.xbm')	
if ( sys.platform.startswith('win')): 
	root.iconbitmap('m_player.ico')
else:
	logo = PhotoImage(file='m_player.gif')
	root.call('wm', 'iconphoto', root._w, logo)


textlabel = Label(root,text = "Ambition is my drug, Success is the only cure")
textlabel.pack()

def play():
	mixer.music.load("a.wav")
	mixer.music.play()


playPhoto = PhotoImage(file="play.png")
playBtn = Button(root,image=playPhoto,command=play)
playBtn.pack()


root.mainloop()