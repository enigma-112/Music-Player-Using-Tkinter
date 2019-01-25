from tkinter import *
root = Tk()

root.title("Galactic Music Player")
#root.iconbitmap('@m_player.xbm')
	
if ( sys.platform.startswith('win')): 
	root.iconbitmap('m_player.ico')
else:
	logo = PhotoImage(file='m_player.gif')
	root.call('wm', 'iconphoto', root._w, logo)

root.mainloop()