from system_manager import system_manager
from ollama_manager import ollama_manager
from webui_manager import webui_manager
from config import config

class HealthCheck:
    @staticmethod
    def run_health_check() -> dict:
        os_info = system_manager.get_os_info()
        ram_info = system_manager.get_ram_info()
        cpu_info = system_manager.get_cpu_info()

        ollama_online = ollama_manager.is_online()
        installed_models = ollama_manager.list_local_models() if ollama_online else []
        running_models = ollama_manager.get_running_models() if ollama_online else []

        webui_online = webui_manager.is_online()

        whisper_status = "AVAILABLE" if config.VOICE_ENABLED else "OPTIONAL/DISABLED"
        tts_status = "AVAILABLE" if config.TTS_ENABLED else "OPTIONAL/DISABLED"

        overall_ready = ollama_online and ram_info["available_gb"] >= 1.0

        report = {
            "windows": f"{os_info['system']} {os_info['release']}",
            "python": "OK",
            "ollama": "ONLINE" if ollama_online else "OFFLINE",
            "open_webui": "ONLINE" if webui_online else "OFFLINE",
            "ram_total_gb": ram_info["total_gb"],
            "ram_available_gb": ram_info["available_gb"],
            "cpu_usage": f"{cpu_info['usage_percent']}%",
            "llm_installed_count": len(installed_models),
            "active_models": running_models,
            "whisper": whisper_status,
            "tts": tts_status,
            "overall_status": "READY" if overall_ready else "WARNING/OFFLINE"
        }
        return report

    @staticmethod
    def print_health_summary():
        report = HealthCheck.run_health_check()
        print("==================================================")
        print("           LOCAL AI HEALTH CHECK                 ")
        print("==================================================")
        print(f" OS           : {report['windows']}")
        print(f" Ollama       : {report['ollama']}")
        print(f" Open WebUI   : {report['open_webui']}")
        print(f" Total RAM    : {report['ram_total_gb']} GB")
        print(f" Available    : {report['ram_available_gb']} GB")
        print(f" Installed    : {report['llm_installed_count']} models")
        print(f" Active Model : {', '.join(report['active_models']) if report['active_models'] else 'None'}")
        print(f" Whisper      : {report['whisper']}")
        print(f" Tamil TTS    : {report['tts']}")
        print(f" Overall      : {report['overall_status']}")
        print("==================================================")

health_check = HealthCheck()
