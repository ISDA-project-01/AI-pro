from tamil_tts import tamil_tts
from config import config
from logger import logger

class TTSManager:
    def __init__(self):
        self.enabled = config.TTS_ENABLED
        self.engine = config.TTS_ENGINE

    def speak(self, text: str, lang: str = "en") -> bool:
        if not self.enabled:
            return False

        if lang == "ta" or "mms-tts-tam" in self.engine:
            return tamil_tts.synthesize(text)
        else:
            logger.info(f"General TTS (English/Other): {text[:30]}...")
            return True

tts_manager = TTSManager()
