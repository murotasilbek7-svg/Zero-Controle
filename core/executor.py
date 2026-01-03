import os
import importlib
import time


COMMANDS_DIR = "commands"
COMMAND_COOLDOWN = 6  # sekund

class CommandExecutor:
    def __init__(self, listener):
        self.listener = listener
        self.handlers = []
        self.last_time = {}  # har bir alias uchun oxirgi bajarilish vaqti
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
                    alias_lower = alias.lower()
                    self.handlers.append({
                        "alias": alias_lower,
                        "execute": execute_fn
                    })
                    self.last_time[alias_lower] = 0  # boshlang‘ich vaqt

                print(f"✅ Command yuklandi: {name}")

            except Exception as e:
                print(f"❌ Xato: {name} → {e}")

    def execute(self, command):
        text = command.get("text", "").lower().strip()
        if not text:
            return

        now = time.time()

        for handler in self.handlers:
            alias = handler["alias"]
            if alias in text:
                # 🚫 ALIAS COOLDAOWN TEKSHIRUV
                if (now - self.last_time.get(alias, 0)) < COMMAND_COOLDOWN:
                    print(f"⏳ '{alias}' buyruq cooldownda — e’tiborsiz qoldirildi")
                    return

                # Cooldownni yangilash
                self.last_time[alias] = now

                print(f"⚙️ Mos alias: {alias}")
                handler["execute"]({})
                self.listener.mute_for_seconds(3)
                print("✅ Buyruq bajarildi")
                return

        


