# core/logger.py
from datetime import datetime

def log(message: str):
    """
    Konsolga log yozadi.
    Format: [YYYY-MM-DD HH:MM:SS] xabar
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {message}")
