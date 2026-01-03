# commands/ish.py
import os
import subprocess
import platform
aliases = [
    "kerakliy dasturlar",
    "Ish"
    
]
def execute(args):

    print("💻 Kerakli dasturlar ishga tushmoqda...")

    programs = [
        # Misol uchun Windows uchun dasturlar yo'llari
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Notepad++\notepad++.exe",
        # kerakli boshqa dasturlarni shu yerga qo'shish mumkin
    ]

    system_name = platform.system()

    for prog in programs:
        try:
            if system_name == "Windows":
                subprocess.Popen(prog)
            elif system_name in ["Linux", "Darwin"]:
                subprocess.Popen([prog])
            print(f"✅ Ishga tushdi: {prog}")
        except Exception as e:
            print(f"⚠️ Xato dastur {prog}: {e}")
