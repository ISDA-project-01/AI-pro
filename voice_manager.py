from whisper_manager import whisper_manager
from tts_manager import tts_manager
from config import config

class VoiceManager:
    def __init__(self):
        self.enabled = config.VOICE_ENABLED

    def process_voice_input(self, audio_file: str) -> str:
        return whisper_manager.transcribe_audio(audio_file)

    def generate_speech(self, text: str, lang: str = "en") -> bool:
        return tts_manager.speak(text, lang=lang)

voice_manager = VoiceManager()
