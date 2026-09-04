from flask import Flask, jsonify, request
from health_check import health_check
from model_manager import model_manager
from ollama_manager import ollama_manager
from chat_manager import chat_manager
from config import config
from logger import logger

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def get_health():
    return jsonify(health_check.run_health_check())

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify({
        "status": "ONLINE",
        "active_model": model_manager.get_active_model(),
        "ollama_online": ollama_manager.is_online()
    })

@app.route("/models", methods=["GET"])
def list_models():
    return jsonify({
        "supported": model_manager.get_supported_models(),
        "installed": model_manager.get_installed_models(),
        "active": model_manager.get_active_model()
    })

@app.route("/models/select", methods=["POST"])
def select_model():
    data = request.json or {}
    model_name = data.get("model")
    if not model_name:
        return jsonify({"error": "Missing model parameter"}), 400

    success = model_manager.switch_model(model_name)
    return jsonify({"success": success, "active_model": model_manager.get_active_model()})

@app.route("/models/stop", methods=["POST"])
def stop_model():
    success = model_manager.unload_active_model()
    return jsonify({"success": success})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json or {}
    message = data.get("message", "")
    model = data.get("model")
    system_prompt = data.get("system")

    if not message:
        return jsonify({"error": "Empty message"}), 400

    response = chat_manager.send_message(message, model=model, system_prompt=system_prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    logger.info(f"Starting Local AI Controller on {config.CONTROLLER_HOST}:{config.CONTROLLER_PORT}")
    app.run(host=config.CONTROLLER_HOST, port=config.CONTROLLER_PORT)
