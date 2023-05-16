from pygame import mixer
from tkinter import *
#Instantiate mixer
mixer.init()

root = Tk() 
#top level window
#Load audio file
mixer.music.load('Rasputin.mp3')

label = Label(root, text="Song Button")
label.pack()

#Set preferred volume
mixer.music.set_volume(0.2)

#Infinite loop
while True:
	print("------------------------------------------------------------------------------------")
	print("Press 'p' to pause the music")
	print("Press 'r' to resume the music")
	print("Press 'e' to exit the program")

	#take user input
	userInput = input(" ")
	
	if userInput == 'p':

		# Pause the music
		mixer.music.pause()	
		print("music is paused....")
	elif userInput == 'r':

		# Resume the music
		mixer.music.unpause()
		print("music is resumed....")
	elif userInput == 'e':

		# Stop the music playback
		mixer.music.stop()
		print("music is stopped....")
		break

def play():
	mixer.music.play()

	
button = Button(root, text='click me!', command=play)
button['state'] = 'disabled' # can disable the button
button['state'] = 'normal' # back to normal
button.pack()

root.geometry("350x300")
root.mainloop()
