import os
import json
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Logger:
    def __init__(self, name="LocalAIController", log_file="logs/app.log", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.handlers = []  # Clear default handlers

        # Formatter (Avoid logging sensitive data or full prompts by default)
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s')

        # Console Handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        # File Handler
        try:
            log_dir = BASE_DIR / "logs"
            log_dir.mkdir(exist_ok=True)
            fh = logging.FileHandler(BASE_DIR / log_file, encoding='utf-8')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        except Exception as e:
            print(f"Warning: Could not set up log file handler: {e}")

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def debug(self, msg):
        self.logger.debug(msg)

logger = Logger()
