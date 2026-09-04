import requests
import json
from config import config
from logger import logger

class OllamaManager:
    def __init__(self, host=None):
        self.host = host or config.OLLAMA_HOST

    def is_online(self) -> bool:
        try:
            r = requests.get(f"{self.host}/", timeout=3)
            return r.status_code == 200
        except Exception:
            return False

    def list_local_models(self) -> list:
        try:
            r = requests.get(f"{self.host}/api/tags", timeout=5)
            if r.status_code == 200:
                data = r.json()
                return [m["name"] for m in data.get("models", [])]
        except Exception as e:
            logger.error(f"Failed to list local models: {e}")
        return []

    def get_running_models(self) -> list:
        try:
            r = requests.get(f"{self.host}/api/ps", timeout=5)
            if r.status_code == 200:
                data = r.json()
                return [m["name"] for m in data.get("models", [])]
        except Exception as e:
            logger.error(f"Failed to list running models: {e}")
        return []

    def stop_model(self, model_name: str) -> bool:
        """Unload a loaded model by sending generate request with keep_alive=0"""
        try:
            payload = {
                "model": model_name,
                "keep_alive": 0
            }
            r = requests.post(f"{self.host}/api/generate", json=payload, timeout=10)
            logger.info(f"Unloaded/stopped model {model_name}")
            return r.status_code == 200
        except Exception as e:
            logger.error(f"Failed to stop model {model_name}: {e}")
            return False

    def stop_all_models(self) -> bool:
        running = self.get_running_models()
        success = True
        for model in running:
            if not self.stop_model(model):
                success = False
        return success

    def pull_model(self, model_tag: str):
        try:
            payload = {"name": model_tag, "stream": False}
            r = requests.post(f"{self.host}/api/pull", json=payload, timeout=600)
            return r.status_code == 200
        except Exception as e:
            logger.error(f"Failed to pull model {model_tag}: {e}")
            return False

    def generate(self, model: str, prompt: str, system: str = None, options: dict = None, stream: bool = False):
        url = f"{self.host}/api/generate"
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": stream
        }
        if system:
            payload["system"] = system
        if options:
            payload["options"] = options
        try:
            r = requests.post(url, json=payload, stream=stream, timeout=120)
            return r
        except Exception as e:
            logger.error(f"Generate request failed: {e}")
            return None

    def chat(self, model: str, messages: list, options: dict = None, stream: bool = False):
        url = f"{self.host}/api/chat"
        payload = {
            "model": model,
            "messages": messages,
            "stream": stream
        }
        if options:
            payload["options"] = options
        try:
            r = requests.post(url, json=payload, stream=stream, timeout=120)
            return r
        except Exception as e:
            logger.error(f"Chat request failed: {e}")
            return None

ollama_manager = OllamaManager()
