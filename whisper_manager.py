from config import config
from logger import logger

class WhisperManager:
    def __init__(self):
        self.model_name = config.WHISPER_MODEL
        self.loaded = False

    def transcribe_audio(self, audio_filepath: str) -> str:
        if not config.VOICE_ENABLED:
            return "Voice processing is currently disabled."

        try:
            import whisper
            # Lazy load whisper model only when invoked to save RAM
            model = whisper.load_model(self.model_name)
            result = model.transcribe(audio_filepath)
            return result.get("text", "")
        except ImportError:
            return "Whisper library is not installed. Install optional audio dependencies."
        except Exception as e:
            logger.error(f"Whisper transcription failed: {e}")
            return f"Audio transcription error: {e}"

whisper_manager = WhisperManager()
