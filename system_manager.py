import psutil
import platform
import shutil
import os
from config import config
from logger import logger

class SystemManager:
    @staticmethod
    def get_os_info() -> dict:
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "architecture": platform.machine()
        }

    @staticmethod
    def get_ram_info() -> dict:
        mem = psutil.virtual_memory()
        return {
            "total_gb": round(mem.total / (1024 ** 3), 2),
            "available_gb": round(mem.available / (1024 ** 3), 2),
            "used_gb": round(mem.used / (1024 ** 3), 2),
            "percent_used": mem.percent,
            "warning": mem.available / (1024 ** 3) < 1.5
        }

    @staticmethod
    def get_cpu_info() -> dict:
        return {
            "cores": psutil.cpu_count(logical=False),
            "threads": psutil.cpu_count(logical=True),
            "usage_percent": psutil.cpu_percent(interval=0.5)
        }

    @staticmethod
    def get_disk_info() -> dict:
        disk = shutil.disk_usage("/")
        return {
            "total_gb": round(disk.total / (1024 ** 3), 2),
            "free_gb": round(disk.free / (1024 ** 3), 2),
            "used_gb": round(disk.used / (1024 ** 3), 2)
        }

    @staticmethod
    def check_port_in_use(port: int) -> bool:
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('127.0.0.1', port)) == 0

system_manager = SystemManager()
