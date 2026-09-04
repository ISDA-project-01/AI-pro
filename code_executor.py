import sys
import io
import contextlib
import time
from config import config
from logger import logger

class CodeExecutor:
    def __init__(self):
        self.enabled = config.CODE_EXECUTION_ENABLED

    def execute_python(self, code: str, timeout_sec: int = 10) -> dict:
        if not self.enabled:
            return {
                "success": False,
                "stdout": "",
                "stderr": "Code execution is disabled by default in settings for security.",
                "execution_time": 0
            }

        start_time = time.time()
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()

        # Restricted execution globals
        safe_globals = {
            "__builtins__": __builtins__,
            "print": print,
            "range": range,
            "len": len,
            "str": str,
            "int": int,
            "float": float,
            "list": list,
            "dict": dict
        }

        try:
            with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
                exec(code, safe_globals)
            exec_time = round(time.time() - start_time, 4)
            return {
                "success": True,
                "stdout": stdout_capture.getvalue(),
                "stderr": stderr_capture.getvalue(),
                "execution_time": exec_time
            }
        except Exception as e:
            exec_time = round(time.time() - start_time, 4)
            return {
                "success": False,
                "stdout": stdout_capture.getvalue(),
                "stderr": str(e),
                "execution_time": exec_time
            }

code_executor = CodeExecutor()
