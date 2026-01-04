import os
aliases = [
    "telegram",
    "teleg",
    "telegramni och",
    "telegni och"
    
]

def execute(args):
    import os

    # Standart o'rnatilish yo'li (Roaming papkasida)
    path = os.path.expandvars(r'%AppData%\Telegram Desktop\Telegram.exe')

    if os.path.exists(path):
        os.startfile(path)
    else:
        print("Telegram topilmadi. Iltimos, o'rnatilgan yo'lni tekshiring.")
