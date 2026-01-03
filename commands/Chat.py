import webbrowser
import pygame
def execute(args):
    webbrowser.open("https://www.chatgpt.com")
    print("🌐 ChatGPT veb-sayti ochildi.")
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/chat.wav")
    pygame.mixer.music.play()
