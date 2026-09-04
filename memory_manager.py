import json
from utils import load_json_file, save_json_file
from config import config
from logger import logger

MEMORY_FILE = "data/memory.json"

class MemoryManager:
    def __init__(self):
        self.enabled = config.MEMORY_ENABLED
        self.memories = load_json_file(MEMORY_FILE, default=[])

    def add_memory(self, fact: str) -> bool:
        if not self.enabled or not fact:
            return False
        # Do not store sensitive secrets
        sensitive_keywords = ["password", "api_key", "token", "secret", "bearer"]
        if any(kw in fact.lower() for kw in sensitive_keywords):
            logger.warning("Attempted to store potential secret in memory. Blocked.")
            return False

        if fact not in self.memories:
            self.memories.append(fact)
            save_json_file(MEMORY_FILE, self.memories)
            logger.info("Memory stored.")
            return True
        return False

    def get_memories(self) -> list:
        return self.memories if self.enabled else []

    def clear_memories(self) -> bool:
        self.memories = []
        return save_json_file(MEMORY_FILE, self.memories)

memory_manager = MemoryManager()
