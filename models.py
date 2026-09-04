SUPPORTED_MODELS = {
    "llama3.2:3b": {
        "name": "Llama 3.2 3B",
        "tag": "llama3.2:3b",
        "size": "2.0 GB",
        "role": "General Chat / Default",
        "description": "Default general-purpose assistant. Ideal for chat, memory, RAG, and web search.",
        "params": {"temperature": 0.7, "top_p": 0.9}
    },
    "gemma2:2b": {
        "name": "Gemma 2 2B",
        "tag": "gemma2:2b",
        "size": "1.6 GB",
        "role": "Fast Chat",
        "description": "Fast lightweight assistant for quick responses, simple Q&A, and summaries.",
        "params": {"temperature": 0.7, "top_p": 0.9}
    },
    "phi3.5:3.8b": {
        "name": "Phi 3.5 3.8B",
        "tag": "phi3.5:3.8b",
        "size": "2.2 GB",
        "role": "Reasoning / General",
        "description": "General reasoning, writing, productivity, analysis, and RAG.",
        "params": {"temperature": 0.7, "top_p": 0.9}
    },
    "qwen2.5-coder:3b": {
        "name": "Qwen2.5-Coder 3B",
        "tag": "qwen2.5-coder:3b",
        "size": "1.9 GB",
        "role": "Coding",
        "description": "Primary programming model for code generation, debugging, terminal, and repository analysis.",
        "params": {"temperature": 0.2, "top_p": 0.95}
    },
    "deepseek-r1:1.5b": {
        "name": "DeepSeek-R1 1.5B",
        "tag": "deepseek-r1:1.5b",
        "size": "1.1 GB",
        "role": "Reasoning",
        "description": "Lightweight reasoning model for mathematical, logical, and step-by-step reasoning.",
        "params": {"temperature": 0.6, "top_p": 0.95}
    },
    "openelm:3b": {
        "name": "OpenELM 3B",
        "tag": "openelm:3b",
        "size": "1.8 GB",
        "role": "Lightweight General",
        "description": "Lightweight general purpose model by Apple.",
        "params": {"temperature": 0.7, "top_p": 0.9}
    },
    "ministral:3b": {
        "name": "Ministral 3B",
        "tag": "ministral:3b",
        "size": "2.1 GB",
        "role": "Balanced / Tools",
        "description": "General assistant and tool-oriented experimentation.",
        "params": {"temperature": 0.7, "top_p": 0.9}
    },
    "smollm2:1.7b": {
        "name": "SmolLM2 1.7B",
        "tag": "smollm2:1.7b",
        "size": "1.0 GB",
        "role": "Fast Assistant",
        "description": "Fastest and lightest assistant for simple tasks and low resource environments.",
        "params": {"temperature": 0.7, "top_p": 0.9}
    }
}

PRESETS = {
    "GENERAL": "llama3.2:3b",
    "FAST": "smollm2:1.7b",
    "CODING": "qwen2.5-coder:3b",
    "REASONING": "deepseek-r1:1.5b",
    "LIGHT_GENERAL": "gemma2:2b",
    "BALANCED": "ministral:3b"
}
