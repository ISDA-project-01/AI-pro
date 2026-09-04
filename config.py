import os
from pathlib import Path
from utils import BASE_DIR

def _get_env_bool(key: str, default: bool) -> bool:
    val = os.getenv(key)
    if val is None:
        return default
    return val.lower() in ("true", "1", "yes", "on")

def _get_env_int(key: str, default: int) -> int:
    val = os.getenv(key)
    if val is None:
        return default
    try:
        return int(val)
    except ValueError:
        return default

def _get_env_float(key: str, default: float) -> float:
    val = os.getenv(key)
    if val is None:
        return default
    try:
        return float(val)
    except ValueError:
        return default

# Load .env file if available
env_file = BASE_DIR / ".env"
if env_file.exists():
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

class Config:
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
    OPEN_WEBUI_URL = os.getenv("OPEN_WEBUI_URL", "http://127.0.0.1:8080")
    CONTROLLER_HOST = os.getenv("CONTROLLER_HOST", "127.0.0.1")
    CONTROLLER_PORT = _get_env_int("CONTROLLER_PORT", 5000)

    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "llama3.2:3b")
    CONTEXT_LENGTH = _get_env_int("CONTEXT_LENGTH", 8192)
    TEMPERATURE = _get_env_float("TEMPERATURE", 0.7)
    TOP_P = _get_env_float("TOP_P", 0.9)
    TOP_K = _get_env_int("TOP_K", 40)
    REPEAT_PENALTY = _get_env_float("REPEAT_PENALTY", 1.1)
    MODEL_TIMEOUT = _get_env_int("MODEL_TIMEOUT", 300)
    AUTO_UNLOAD_MINUTES = _get_env_int("AUTO_UNLOAD_MINUTES", 15)

    WEB_SEARCH_ENABLED = _get_env_bool("WEB_SEARCH_ENABLED", False)
    RAG_ENABLED = _get_env_bool("RAG_ENABLED", True)
    MEMORY_ENABLED = _get_env_bool("MEMORY_ENABLED", True)
    CODE_EXECUTION_ENABLED = _get_env_bool("CODE_EXECUTION_ENABLED", False)
    TERMINAL_ENABLED = _get_env_bool("TERMINAL_ENABLED", False)
    VOICE_ENABLED = _get_env_bool("VOICE_ENABLED", False)
    TTS_ENABLED = _get_env_bool("TTS_ENABLED", False)

    WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base")
    TTS_ENGINE = os.getenv("TTS_ENGINE", "mms-tts-tam")

    SEARCH_PROVIDER = os.getenv("SEARCH_PROVIDER", "duckduckgo")
    SEARCH_API_KEY = os.getenv("SEARCH_API_KEY", "")

    MAX_RAM_GB = 8
    ENFORCE_SINGLE_MODEL = True

config = Config()
