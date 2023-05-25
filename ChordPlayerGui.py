import pygame
from tkinter import *
from tkinter import ttk
import tkinter as tk

pygame.mixer.init()

# Define song choices
song_choices = {
    "Rasputin": "Rasputin.mp3",
    "Stairway To Heaven": "stairway_to_heaven.mp3",
    "Zombie": "zombie.wav",
    "Duel of the Fates": "Duel of the Fates.mp3",
    "The Chain": "Fleetwood Mac - The Chain.mp3"
}

# Function to play selected song
def play_song():
    song_choice = song_listbox.get(song_listbox.curselection())
    song_path = song_choices[song_choice]
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Function to resume the music
def resume_music():
    pygame.mixer.music.unpause()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Function to seek through the song
def seek_music(position):
    song_choice = song_listbox.get(song_listbox.curselection())
    song_path = song_choices[song_choice]
    sound = pygame.mixer.Sound(song_path)
    sound_length = sound.get_length()
    seek_time = sound_length * float(position)
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(start=int(seek_time))

root = Tk() # Top-level window
root.title("Song Player")

# Create a listbox to display song choices
song_listbox = Listbox(root, width=30)
song_listbox.pack(pady=10)

# Insert song choices into the listbox
for song in song_choices:
    song_listbox.insert(END, song)

#Create button images
click_but= PhotoImage(file='playbutton.png')

# Create buttons for controlling the music playback
play_button = Button(root, image=click_but, command=play_song)
pause_button = Button(root, text="Pause", command=pause_music)
resume_button = Button(root, text="Resume", command=resume_music)
stop_button = Button(root, text="Stop", command=stop_music)

play_button.pack(side=LEFT, padx=5)
pause_button.pack(side=LEFT, padx=5)
resume_button.pack(side=LEFT, padx=5)
stop_button.pack(side=LEFT, padx=5)

# Create a Scale widget for seeking through the song
seek_scale = Scale(root, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, length=200, command=seek_music)
seek_scale.pack(pady=10)

root.geometry("480x480")
root.mainloop()
