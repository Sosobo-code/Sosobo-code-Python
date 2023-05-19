from pygame import mixer
from tkinter import *
from tkinter import ttk
import tkinter as tk
#Instantiate mixer
mixer.init()

def pauseandplayinputs():

	userInput = entry2.get()
	
	if userInput == 'p':

		# Pause the music
		mixer.music.pause()	
	elif userInput == 'r':

		# Resume the music
		mixer.music.unpause()
	elif userInput == 'e':

		# Stop the music playback
		mixer.music.stop()

root = Tk() #top level window
#Load audio file
mixer.music.load('Rasputin.mp3')
label = Label(root, text="Song Player")
label.pack()

#Make entry box
entry = ttk.Entry(root, width=30)
entry.insert(0, "Enter (r) for resume, (p) for pause, (e) for end.")
entry2 = ttk.Entry(root, width=30)
entry.pack()
entry2.pack()

button = tk.Button(root, text='Submit', command=pauseandplayinputs)
button.pack(pady=10)
#Set preferred volume
mixer.music.set_volume(0.2)


def play():
	mixer.music.play()
def disablebutton():
	button['state'] = 'disabled' # can disable the button
def enablebutton():
	button['state'] = 'normal'
button = Button(root, text='click me to play song.', command=play)
button2 = Button(root, text='Click me to disable play button.', command=disablebutton)
button3 = Button(root, text='Click me to enable play button.', command=enablebutton)
button.pack()
button2.pack()
button3.pack()

root.geometry("350x300")
root.mainloop()
