import webbrowser
import pygame
import time

aliases = [
    "google",
    "googl",
    "bu",
    "google ga kir",
    "googl ga kir",
    "go'yo",


]
def execute(args):
    webbrowser.open("https://google.com")
    print("🌐 Google veb-sayti ochildi.")
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/google.wav")
    pygame.mixer.music.play()
