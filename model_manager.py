from models import SUPPORTED_MODELS, PRESETS
from ollama_manager import ollama_manager
from config import config
from logger import logger

class ModelManager:
    def __init__(self):
        self.active_model = config.DEFAULT_MODEL

    def get_supported_models(self) -> dict:
        return SUPPORTED_MODELS

    def get_presets(self) -> dict:
        return PRESETS

    def get_installed_models(self) -> list:
        return ollama_manager.list_local_models()

    def get_active_model(self) -> str:
        running = ollama_manager.get_running_models()
        if running:
            # First running model is current active
            return running[0]
        return self.active_model

    def switch_model(self, target_model: str) -> bool:
        """
        Enforce ONE-MODEL-AT-A-TIME policy.
        Unload current running model before switching to target model.
        """
        logger.info(f"Switching model to: {target_model}")

        # Unload all currently running models to preserve RAM
        if config.ENFORCE_SINGLE_MODEL:
            ollama_manager.stop_all_models()

        self.active_model = target_model
        logger.info(f"Active model set to {target_model}")
        return True

    def unload_active_model(self) -> bool:
        return ollama_manager.stop_all_models()

    def install_model(self, model_tag: str) -> bool:
        logger.info(f"Installing model {model_tag}...")
        return ollama_manager.pull_model(model_tag)

model_manager = ModelManager()
