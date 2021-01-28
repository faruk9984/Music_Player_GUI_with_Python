# Music Player GUI with Python

import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

music_player=tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("450x350")
directory=askdirectory()
os.chdir(directory)
song_list=os.listdir()

play_list=tkr.Listbox(music_player,font='Helvetica 12 bold',
                      bg='yellow',selectmode=tkr.SINGLE)
for item in song_list:
    pos=0
    play_list.insert(pos,item)
    pos+=1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

button1=tkr.Button(music_player,width=5,height=3,font='Helvetca 12 bold',text='PLAY',command=play,bg='blue',fg='white')
button2=tkr.Button(music_player,width=5,height=3,font='Helvetca 12 bold',text='STOP',command=stop,bg='red',fg='white')
button3=tkr.Button(music_player,width=5,height=3,font='Helvetca 12 bold',text='PAUSE',command=pause,bg='purple',fg='white')
button4=tkr.Button(music_player,width=5,height=3,font='Helvetca 12 bold',text='UNPAUSE',command=unpause,bg='orange',fg='white')

var=tkr.StringVar()
song_title=tkr.Label(music_player,font='Helvetca 12 bold',textvariable=var)

song_title.pack()
button1.pack(fill='x')
button2.pack(fill='x')
button3.pack(fill='x')
button4.pack(fill='x')
play_list.pack(fill='both',expand='yes')
music_player.mainloop()


