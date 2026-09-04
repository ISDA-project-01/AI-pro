import requests
from config import config
from logger import logger
import webbrowser

class WebUIManager:
    def __init__(self, url=None):
        self.url = url or config.OPEN_WEBUI_URL

    def is_online(self) -> bool:
        try:
            r = requests.get(self.url, timeout=3)
            return r.status_code == 200
        except Exception:
            return False

    def open_browser(self):
        try:
            webbrowser.open(self.url)
            logger.info(f"Opened browser to {self.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to open browser: {e}")
            return False

webui_manager = WebUIManager()
