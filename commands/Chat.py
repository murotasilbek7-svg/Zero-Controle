import webbrowser
import pygame
aliases = [
    "chatgpt",
    "chat gpt",
    "chat",
    "AI",
    "chap",
    "chad",
    "i AIga kir"


]
def execute(args):
    webbrowser.open("https://www.chatgpt.com")
    print("🌐 ChatGPT veb-sayti ochildi.")
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/chat.wav")
    pygame.mixer.music.play()
