#main.py
from core.listener import VoiceListener
from core.executor import CommandExecutor

def main():
    listener = VoiceListener(uz_model_path="model/vosk-model-small-uz-0.22")
    executor = CommandExecutor()
    

    print("🔵 Zero Controle fon rejimida ishga tushdi...")

    for command in listener.listen():  # generator ichida doimiy eshitadi
        executor.execute(command)

if __name__ == "__main__":
    main()
