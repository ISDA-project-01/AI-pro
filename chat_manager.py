from ollama_manager import ollama_manager
from model_manager import model_manager
from config import config
from logger import logger

class ChatManager:
    def send_message(self, message: str, model: str = None, system_prompt: str = None) -> str:
        target_model = model or model_manager.get_active_model()

        # Ensure target model is loaded in 1-model policy
        model_manager.switch_model(target_model)

        options = {
            "num_ctx": config.CONTEXT_LENGTH,
            "temperature": config.TEMPERATURE,
            "top_p": config.TOP_P,
            "top_k": config.TOP_K,
            "repeat_penalty": config.REPEAT_PENALTY
        }

        res = ollama_manager.generate(
            model=target_model,
            prompt=message,
            system=system_prompt,
            options=options,
            stream=False
        )

        if res and res.status_code == 200:
            return res.json().get("response", "")
        else:
            return "Error: Unable to generate response from Ollama."

chat_manager = ChatManager()
