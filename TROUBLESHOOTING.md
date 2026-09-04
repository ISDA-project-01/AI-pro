# Troubleshooting Guide

## Common Issues & Solutions

### 1. Ollama standard API offline
- **Symptom**: `Ollama: OFFLINE` in health check.
- **Solution**: Ensure Ollama is running in the Windows system tray or run `ollama serve` in CMD.

### 2. High RAM Usage / Out of Memory
- **Symptom**: Windows becomes sluggish.
- **Solution**: Run `python main.py unload` to free RAM. Close background applications.

### 3. Open WebUI Connection Error
- **Symptom**: Browser cannot connect to `http://127.0.0.1:8080`.
- **Solution**: Check if Open WebUI container or server process is active.
