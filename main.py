import sys
import argparse
from health_check import health_check
from model_manager import model_manager
from ollama_manager import ollama_manager
from webui_manager import webui_manager
from chat_manager import chat_manager
from config import config

def show_banner():
    print("""
╔══════════════════════════════════════════════════════════╗
║               LOCAL AI ASSISTANT PLATFORM                ║
╠══════════════════════════════════════════════════════════╣
║ Ollama Status : ONLINE                                   ║
║ Target System : Windows 10 (8 GB RAM / CPU-only)         ║
║ Policy        : 1 Active LLM at a time                   ║
╚══════════════════════════════════════════════════════════╝
""")

def main():
    parser = argparse.ArgumentParser(description="Local AI Assistant Controller CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("health", help="Run system health check")
    subparsers.add_parser("status", help="Show platform status")
    subparsers.add_parser("models", help="List installed & supported models")

    switch_parser = subparsers.add_parser("switch-model", help="Switch active model")
    switch_parser.add_argument("model", type=str, help="Model tag (e.g., qwen2.5-coder:3b)")

    install_parser = subparsers.add_parser("install-model", help="Pull/Install model")
    install_parser.add_argument("model", type=str, help="Model tag to pull")

    subparsers.add_parser("unload", help="Unload running models from RAM")

    chat_parser = subparsers.add_parser("chat", help="Send chat message")
    chat_parser.add_argument("message", type=str, help="Prompt text")

    args = parser.parse_args()

    if args.command == "health":
        health_check.print_health_summary()
    elif args.command == "status":
        show_banner()
        print(f"Active Model: {model_manager.get_active_model()}")
        print(f"Ollama: {'ONLINE' if ollama_manager.is_online() else 'OFFLINE'}")
        print(f"Open WebUI: {'ONLINE' if webui_manager.is_online() else 'OFFLINE'}")
    elif args.command == "models":
        print("\nSupported Models:")
        for tag, info in model_manager.get_supported_models().items():
            print(f" - {tag} [{info['name']}] -> {info['role']}")
        print("\nInstalled Local Models:")
        for m in model_manager.get_installed_models():
            print(f" * {m}")
    elif args.command == "switch-model":
        model_manager.switch_model(args.model)
        print(f"Switched active model to: {args.model}")
    elif args.command == "install-model":
        print(f"Pulling model {args.model}...")
        res = model_manager.install_model(args.model)
        print("Installation finished successfully!" if res else "Installation failed.")
    elif args.command == "unload":
        model_manager.unload_active_model()
        print("Unloaded all models from memory.")
    elif args.command == "chat":
        res = chat_manager.send_message(args.message)
        print(f"\nResponse:\n{res}")
    else:
        show_banner()
        health_check.print_health_summary()

if __name__ == "__main__":
    main()
