# commands/shutdown.py
import os
import platform

aliases = [
    "o‘chir",
    "ochir",
    "shutdown",
    "kompyuterni o‘chir",
    "sistemani o‘chir"
]
def execute(args):
    """
    Kompyuterni o'chiradi
    """
    system_name = platform.system()
    print("🛑 Sistemani o'chirish ishga tushdi...")

    try:
        if system_name == "Windows":
            os.system("shutdown /s /t 5")  # 5 soniyadan keyin o'chadi
        elif system_name == "Linux":
            os.system("shutdown now")
        elif system_name == "Darwin":  # macOS
            os.system("sudo shutdown -h now")
        else:
            print(f"⚠️ Unknown OS: {system_name}")
    except Exception as e:
        print(f"⚠️ Xato: {e}")
