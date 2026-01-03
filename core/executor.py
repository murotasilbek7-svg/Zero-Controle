import os
import importlib
import time

COMMANDS_DIR = "commands"
COMMAND_COOLDOWN = 6  # sekund

class CommandExecutor:
    def __init__(self):
        self.handlers = []
        self.last_text = None
        self.last_time = 0
        self.load_commands()

    def load_commands(self):
        for fname in os.listdir(COMMANDS_DIR):
            if not fname.endswith(".py") or fname == "__init__.py":
                continue

            name = fname[:-3]
            module_path = f"{COMMANDS_DIR}.{name}".replace("\\", ".")

            try:
                module = importlib.import_module(module_path)
                aliases = getattr(module, "aliases", [])
                execute_fn = getattr(module, "execute", None)

                if not aliases or not execute_fn:
                    print(f"⚠️ {name}.py → aliases yoki execute yo‘q")
                    continue

                for alias in aliases:
                    self.handlers.append({
                        "alias": alias.lower(),
                        "execute": execute_fn
                    })

                print(f"✅ Command yuklandi: {name}")

            except Exception as e:
                print(f"❌ Xato: {name} → {e}")

    def execute(self, command):
        text = command.get("text", "").lower().strip()
        if not text:
            return

        now = time.time()

        # 🚫 BIR XIL BUYRUQNI QAYTA-QAYTA BAJARMASLIK
        if text == self.last_text and (now - self.last_time) < COMMAND_COOLDOWN:
            print("⏳ Takroriy buyruq — e’tiborsiz qoldirildi")
            return

        self.last_text = text
        self.last_time = now

        for handler in self.handlers:
            if handler["alias"] in text:
                print(f"⚙️ Mos alias: {handler['alias']}")
                handler["execute"]({})
                print("✅ Buyruq bajarildi")
                return

        print("❔ Mos buyruq topilmadi")
