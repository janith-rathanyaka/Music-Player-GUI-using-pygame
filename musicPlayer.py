import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()

musicplayer.title("Music Player")

musicplayer.geometry("450x350")
directory = askdirectory()

os.chdir(directory)

songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font = "Canbria 14 bold", bg ="cyan2" , selectmode = tkr.SINGLE)

for item in songlist:
    pos=0
    playlist.insert(pos, item)
    pos=pos+1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()