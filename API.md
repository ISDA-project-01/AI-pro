# Controller API Documentation

The controller exposes REST API endpoints on `http://127.0.0.1:5000`.

## Endpoints

### `GET /health`
Returns system status report including RAM, CPU, Ollama, and Open WebUI status.

### `GET /models`
Returns list of supported, installed, and active models.

### `POST /models/select`
Switches active model and unloads previous models from memory.
- **Body**: `{"model": "qwen2.5-coder:3b"}`

### `POST /models/stop`
Unloads all loaded models from RAM.

### `POST /chat`
Sends prompt to active model.
- **Body**: `{"message": "Hello!", "model": "llama3.2:3b"}`
