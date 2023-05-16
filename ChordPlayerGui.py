from pygame import mixer
#Instantiate mixer
mixer.init()

#top level window
#Load audio file
mixer.music.load('Rasputin.mp3')


#Set preferred volume
mixer.music.set_volume(0.2)

mixer.music.play()
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

