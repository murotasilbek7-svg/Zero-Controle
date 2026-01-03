import webbrowser
import pygame
import time
aliases = [
    "youtube",
    "yutub",
    "yutuq",
    "yutubga kir",
    "yutuqga kir",
    "youtube ga kir",
    "yutib"
    ]
def execute(args):
    webbrowser.open("https://www.youtube.com")
    print("🌐 YouTube veb-sayti ochildi.")
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/youtube.wav")
    pygame.mixer.music.play()
