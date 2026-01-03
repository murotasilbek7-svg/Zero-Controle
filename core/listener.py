import sounddevice as sd
import queue
import json
import time
from vosk import Model, KaldiRecognizer

class VoiceListener:
    def __init__(self, uz_model_path):
        self.q = queue.Queue()
        self.model = Model(uz_model_path)
        self.rec = KaldiRecognizer(self.model, 16000)
        self.mute_until = 0

        self.stream = sd.RawInputStream(
            samplerate=16000,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=self._callback
        )
        self.stream.start()
        print("🎧 Mikrofon tinglash boshlandi...")

    def _callback(self, indata, frames, time_info, status):
        if time.time() < self.mute_until:
            return
        self.q.put(bytes(indata))

    def mute_for_seconds(self, seconds):
        self.mute_until = time.time() + seconds

    def listen(self):
        """Generator sifatida doimiy eshitish"""
        while True:
            data = self.q.get()
            if self.rec.AcceptWaveform(data):
                result = json.loads(self.rec.Result())
                text = result.get("text", "").strip()

                if text:
                    # 🔥 DEBUG: har bir eshitilgan gap
                    print(f"🎤 Eshitildi: {text}")
                    yield {"text": text}
