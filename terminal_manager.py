import subprocess
from config import config
from logger import logger
from utils import is_windows

class TerminalManager:
    def __init__(self):
        self.enabled = config.TERMINAL_ENABLED

    def run_command(self, command: str, approved: bool = False) -> dict:
        if not self.enabled:
            return {
                "success": False,
                "output": "",
                "error": "Terminal execution is disabled in config."
            }

        if not approved:
            # Require explicit approval for terminal commands
            return {
                "success": False,
                "output": "",
                "error": "Command approval required before executing terminal command."
            }

        # Check dangerous patterns
        dangerous_keywords = ["rmdir /s", "del /f", "format", "rm -rf", "drop database", "mkfs"]
        if any(dk in command.lower() for dk in dangerous_keywords):
            logger.warning(f"Blocked dangerous command: {command}")
            return {
                "success": False,
                "output": "",
                "error": "Destructive / dangerous command blocked by security check."
            }

        try:
            res = subprocess.run(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30
            )
            return {
                "success": res.returncode == 0,
                "output": res.stdout.strip(),
                "error": res.stderr.strip()
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": str(e)
            }

terminal_manager = TerminalManager()
