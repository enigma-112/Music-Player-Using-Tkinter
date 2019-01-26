from tkinter import *		#importing tkinter
from pygame import mixer	#importing mixer from pygame
root = Tk()					#intializing the tkinter window

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
	mixer.music.load("a.wav")
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
scale.pack()








root.mainloop()