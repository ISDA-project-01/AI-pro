# JULES MASTER PROMPT — LOCAL CHATGPT-STYLE AI SYSTEM

## 1. PROJECT OBJECTIVE

Build a complete, production-quality **local AI assistant platform** for Windows 10 using **Ollama as the local LLM runtime** and **Open WebUI as the primary web interface**.

The project must be designed specifically for a computer with:

- Windows 10
- 8 GB RAM
- CPU-only
- No dedicated GPU
- Only ONE LLM loaded/running at a time
- Lightweight local AI models
- No image generation
- No video generation
- Free/open-source components wherever practical
- No requirement for cloud AI

The goal is to create a local system that provides as many practical ChatGPT-style features as possible without requiring a powerful GPU or multiple simultaneously loaded models.

The project must be usable by a beginner but structured professionally enough for development and future expansion.

---

# 2. IMPORTANT JULES REQUIREMENTS

You MUST:

1. Actually create the complete project files.
2. Do not merely describe the files.
3. Do not leave important files as placeholders.
4. Write functional code wherever functionality is requested.
5. Create exactly the 49 files listed in this specification.
6. Do not silently add additional source files.
7. Keep the system optimized for 8 GB RAM and CPU-only operation.
8. Never intentionally load multiple LLMs simultaneously.
9. Provide model switching.
10. Provide automatic model unloading.
11. Make setup as automated as possible.
12. Make all Windows setup scripts work with standard Windows 10.
13. Detect missing dependencies and provide useful error messages.
14. Avoid requiring a dedicated GPU.
15. Do not include image-generation or video-generation functionality.
16. Clearly document third-party licenses.
17. Never hard-code API keys, passwords, tokens, or private credentials.
18. Use configuration files/environment variables for configurable secrets.
19. Make the project safe by default.
20. Make the project easy to uninstall or reset.
21. Verify all code for syntax errors and obvious runtime problems before finishing.
22. Keep documentation synchronized with the implementation.
23. Do not claim a feature works if the implementation does not support it.
24. Prefer local processing whenever possible.
25. Use official Ollama/Open WebUI interfaces and APIs rather than fragile hacks.

---

# 3. 49-FILE PROJECT STRUCTURE

Create exactly these 49 files:

```text
local-ai-assistant/
│
├── README.md
├── LICENSE.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── ACKNOWLEDGEMENTS.md
├── CHANGELOG.md
├── INFORMATION.md
├── SETUP_GUIDE.md
├── REQUIREMENTS.md
├── ARCHITECTURE.md
├── PROJECT_STRUCTURE.md
├── MODEL_GUIDE.md
├── TOOL_LICENSES.md
├── PRIVACY.md
├── TROUBLESHOOTING.md
├── FAQ.md
├── API.md
├── CONFIGURATION.md
├── PERFORMANCE.md
├── RESOURCE_USAGE.md
├── ROADMAP.md
├── .gitignore
├── .env.example
│
├── index.html
├── main.py
├── app.py
├── config.py
├── models.py
├── ollama_manager.py
├── model_manager.py
├── webui_manager.py
├── memory_manager.py
├── rag_manager.py
├── document_manager.py
├── web_search.py
├── tool_manager.py
├── code_executor.py
├── terminal_manager.py
├── voice_manager.py
├── whisper_manager.py
├── tts_manager.py
├── tamil_tts.py
├── chat_manager.py
├── system_manager.py
├── health_check.py
├── logger.py
├── utils.py
│
├── setup.ps1
├── setup.bat
├── start.bat
├── stop.bat
└── requirements.txt
```

There must be **exactly 49 files**.

---

# 4. CORE TECHNOLOGY

Use this architecture:

```text
Windows 10
    │
    ├── Ollama
    │     │
    │     ├── Llama 3.2 3B
    │     ├── Gemma 2 2B
    │     ├── Phi 3.5 3.8B
    │     ├── Qwen2.5-Coder 3B
    │     ├── DeepSeek-R1 1.5B
    │     ├── OpenELM 3B
    │     ├── Ministral 3B
    │     └── SmolLM2 1.7B
    │
    ├── Whisper-base
    │
    └── Tamil TTS
          ├── AI4Bharat VITS-Rasa
          └── Facebook MMS-TTS-TAM
           
             ↓

        Local AI Controller
             │
             ↓
        Open WebUI
             │
      ┌──────┼─────────┐
      ↓      ↓         ↓
     Chat   RAG      Tools
      │      │         │
      ↓      ↓         ↓
   Memory  Files    Code/Terminal
      │
      ↓
   Voice
```

The Python application should act primarily as an **orchestration/controller layer** around Ollama and Open WebUI, rather than attempting to replace Open WebUI.

---

# 5. SUPPORTED LLM MODELS

Support these models:

```text
llama3.2:3b
gemma2:2b
phi3.5:3.8b
qwen2.5-coder:3b
deepseek-r1:1.5b
openelm:3b
ministral:3b
smollm2:1.7b
```

Important:

- Verify the exact currently available Ollama model tags before implementing installation commands.
- If a requested tag has changed or is unavailable, clearly document the closest official/current equivalent.
- Do NOT silently substitute an unrelated model.
- Make model names configurable in `config.py` or `config.json` if needed.
- The UI must show the currently selected model.

---

# 6. MODEL ROLES

Configure sensible roles:

### Llama 3.2 3B

Default general-purpose assistant.

```text
Role:
General Chat

Recommended:
Chat
Memory
RAG
Web Search
Simple Tools
```

### Gemma 2 2B

Fast lightweight general assistant.

```text
Role:
Fast Chat

Recommended:
Simple questions
Summaries
General conversation
```

### Phi 3.5 3.8B

General reasoning and productivity.

```text
Role:
Reasoning / General

Recommended:
Reasoning
Writing
Analysis
RAG
```

### Qwen2.5-Coder 3B

Primary programming model.

```text
Role:
Coding

Recommended:
Programming
Debugging
Code explanation
Code generation
Terminal
Code execution
Repository analysis
```

### DeepSeek-R1 1.5B

Lightweight reasoning model.

```text
Role:
Reasoning

Recommended:
Mathematical reasoning
Logical reasoning
Step-by-step tasks
```

Do not expose hidden chain-of-thought. If the model provides reasoning traces, handle them according to the model/runtime behavior and do not implement a feature intended to expose private internal reasoning.

### OpenELM 3B

Lightweight general model.

### Ministral 3B

General assistant and tool-oriented experimentation.

### SmolLM2 1.7B

Fastest/lightest assistant for simple tasks.

---

# 7. ONE-MODEL-AT-A-TIME REQUIREMENT

This is one of the most important requirements.

The system MUST prioritize:

```text
ONE LLM
+
ONE active inference
+
8 GB RAM
+
CPU
```

Never intentionally keep all eight LLMs loaded simultaneously.

Implement:

```text
Model selection
     ↓
Check currently loaded model
     ↓
Unload/stop previous model if necessary
     ↓
Load selected model
     ↓
Run request
```

Provide model lifecycle functions in:

```text
ollama_manager.py
model_manager.py
```

Include:

- list models
- pull model
- delete model
- run model
- stop model
- check running models
- switch model
- unload model
- health check
- model information
- model size
- RAM recommendations

---

# 8. RAM OPTIMIZATION

Target:

```text
RAM = 8 GB
GPU = unavailable
CPU = primary inference device
```

Use conservative defaults.

Recommended initial context:

```text
4096–8192 tokens
```

Do not automatically configure extremely large context windows.

Make context configurable.

Example configuration:

```text
context_length = 8192
temperature = 0.7
top_p = 0.9
top_k = 40
repeat_penalty = 1.1
```

For coding:

```text
temperature = 0.2
```

Allow per-model configuration.

The system should warn the user when:

- available RAM is low
- Windows is heavily using virtual memory
- another model is running
- a model is too large for the recommended configuration
- multiple AI components are consuming excessive resources

---

# 9. OPEN WEBUI INTEGRATION

Open WebUI is the main user interface.

The project must support connecting Open WebUI to Ollama.

The documentation must explain:

```text
Ollama
  ↓
localhost API
  ↓
Open WebUI
```

The controller should detect whether:

```text
Ollama
```

is available.

It should also detect whether:

```text
Open WebUI
```

is available.

Provide useful health-check messages.

Example:

```text
Ollama: ONLINE
Open WebUI: ONLINE
Models: READY
Voice: AVAILABLE/UNAVAILABLE
TTS: AVAILABLE/UNAVAILABLE
RAM: OK/WARNING
```

---

# 10. CHAT FEATURES

Support/configure Open WebUI features including:

- Chat
- Conversation history
- Search conversations
- Rename conversations
- Delete conversations
- Export conversations
- Markdown
- Code blocks
- Regenerate
- Stop generation
- Edit messages
- Continue response
- Model switching
- System prompts
- Custom model presets
- Files
- Knowledge/RAG
- Memory
- Web search
- Tools
- Code execution
- Terminal integration
- Voice input
- Text-to-speech
- Notes
- Channels
- Authentication
- User management where supported
- API access where supported

Do not recreate Open WebUI unnecessarily.

Use Open WebUI's native functionality whenever possible.

---

# 11. MEMORY

Implement/document integration with Open WebUI memory.

The system should support:

```text
User preferences
Project information
Useful persistent facts
Conversation-related context
```

Provide controls to:

- enable/disable memory
- view memory
- delete memory
- reset memory
- explain privacy implications

Never store passwords, API keys, authentication tokens, or other secrets in memory.

---

# 12. RAG / KNOWLEDGE

Support local document-based retrieval.

Target documents:

```text
PDF
TXT
DOCX
CSV
Markdown
source code
documentation
```

Provide a RAG manager that can:

- ingest documents
- identify supported formats
- create embeddings using a lightweight local embedding model where supported
- retrieve relevant chunks
- provide context to the LLM
- handle errors
- avoid unnecessary RAM usage

Use conservative chunking and retrieval defaults suitable for an 8 GB system.

---

# 13. WEB SEARCH

Support web search through Open WebUI where configured.

Provide configuration for a search provider.

Do not hard-code API keys.

Use environment variables.

Example:

```text
SEARCH_PROVIDER=
SEARCH_API_KEY=
```

The user should be able to disable web search completely.

Clearly distinguish:

```text
LOCAL KNOWLEDGE
```

from:

```text
LIVE WEB INFORMATION
```

The UI/documentation should not falsely claim that a local model has current internet knowledge without web search.

---

# 14. URL / WEB PAGE READING

Where supported by Open WebUI tools:

```text
URL
 ↓
Fetch
 ↓
Extract text
 ↓
LLM
```

Allow the model to summarize or analyze web pages.

Implement safe URL handling.

Do not allow arbitrary dangerous local-file access through a URL feature.

---

# 15. CODE EXECUTION

Provide code-execution support where Open WebUI supports it.

The system should support:

```text
Python
```

as the primary language.

Possible use cases:

- calculations
- CSV analysis
- data processing
- plotting
- simple scripts
- educational programming
- code testing

Security requirements:

- Prefer isolated execution.
- Do not run arbitrary code as administrator.
- Clearly warn about terminal/code execution.
- Never automatically execute destructive commands.
- Do not expose system secrets.
- Provide a way to disable code execution.

---

# 16. TERMINAL

Support an optional terminal/tool integration.

The AI must NOT automatically receive unrestricted administrative privileges.

Commands that could:

```text
delete files
format drives
modify system settings
install software
change firewall settings
change security settings
```

must require explicit user approval.

Never implement a hidden bypass.

Provide:

```text
ALLOW ONCE
ALLOW THIS SESSION
DENY
```

where practical.

---

# 17. VOICE INPUT

Integrate:

```text
Whisper-base
```

for speech-to-text.

Pipeline:

```text
Microphone
 ↓
Whisper
 ↓
Text
 ↓
LLM
```

Support:

- English
- Tamil where Whisper supports it
- other Whisper-supported languages

Make Whisper optional.

Do not load Whisper unnecessarily while it is not being used.

---

# 18. TAMIL TEXT-TO-SPEECH

Support either:

```text
AI4Bharat VITS-Rasa
```

or:

```text
facebook/mms-tts-tam
```

The implementation should allow the user to select/configure the available Tamil TTS backend.

Pipeline:

```text
LLM response
 ↓
Tamil text
 ↓
TTS
 ↓
Audio
```

Make TTS optional.

Do not require both TTS engines to be loaded simultaneously.

---

# 19. LANGUAGE SUPPORT

The interface should work primarily in:

```text
English
Tamil
```

and should not artificially restrict the LLM from responding in other languages supported by the selected model.

Include language configuration.

---

# 20. SYSTEM HEALTH MONITOR

`health_check.py` must check:

- Windows version
- Python
- Ollama
- Open WebUI
- available RAM
- CPU
- installed models
- running models
- Whisper availability
- TTS availability
- network connectivity when web search is enabled
- disk space

Example output:

```text
================================
 LOCAL AI HEALTH CHECK
================================

Windows       : OK
Python        : OK
Ollama        : ONLINE
Open WebUI    : ONLINE

RAM           : 8 GB
Available RAM : XX GB
CPU           : OK

LLM Models    : 8 installed
Active Model  : llama3.2:3b

Whisper       : AVAILABLE
Tamil TTS     : AVAILABLE

Overall       : READY
================================
```

---

# 21. SYSTEM MANAGEMENT

`system_manager.py` should provide safe functions for:

- detecting operating system
- detecting RAM
- detecting CPU
- detecting disk space
- checking processes
- launching services
- stopping services
- checking ports
- environment information

Do not make destructive system modifications.

---

# 22. CONFIGURATION

`config.py` must centralize configuration.

Allow configuration of:

```text
OLLAMA_HOST
OPEN_WEBUI_URL
DEFAULT_MODEL
CONTEXT_LENGTH
TEMPERATURE
TOP_P
TOP_K
REPEAT_PENALTY
MODEL_TIMEOUT
WEB_SEARCH_ENABLED
VOICE_ENABLED
WHISPER_MODEL
TTS_ENGINE
RAG_ENABLED
MEMORY_ENABLED
CODE_EXECUTION_ENABLED
TERMINAL_ENABLED
```

Use safe defaults.

Do not hard-code secrets.

---

# 23. LOGGING

`logger.py` must provide useful logs.

Support:

```text
INFO
WARNING
ERROR
DEBUG
```

Do not log:

- passwords
- API keys
- authentication tokens
- private conversation contents unless explicitly configured
- sensitive environment variables

---

# 24. ERROR HANDLING

Every major component must have clear error handling.

Examples:

```text
Ollama not installed
Ollama not running
Model not installed
Model unavailable
Open WebUI unavailable
Insufficient RAM
Whisper missing
TTS missing
Python dependency missing
Network unavailable
Port already in use
Permission denied
```

Errors should explain:

1. What happened.
2. Why it happened if known.
3. What the user can do.

---

# 25. SETUP.PS1

Create a robust PowerShell installer.

It should:

1. Detect Windows version.
2. Detect Python.
3. Detect Ollama.
4. Check whether Open WebUI is installed.
5. Install missing Python dependencies.
6. Create necessary directories.
7. Create configuration files where necessary.
8. Pull selected Ollama models.
9. Configure the environment.
10. Run health checks.
11. Explain failures clearly.
12. Avoid administrator privileges unless genuinely required.
13. Never download suspicious/untrusted executables.
14. Ask before performing destructive actions.

The script should support useful options such as:

```powershell
.\setup.ps1
.\setup.ps1 -SkipModels
.\setup.ps1 -CheckOnly
```

Do not assume these exact options if another clean design is better, but provide equivalent functionality.

---

# 26. SETUP.BAT

Create a Windows CMD wrapper for users who do not want to open PowerShell.

It should launch:

```text
setup.ps1
```

with appropriate execution handling.

---

# 27. START.BAT

Create a simple launcher that:

1. Starts Ollama if necessary.
2. Starts the local Python controller if needed.
3. Starts/opens Open WebUI if configured.
4. Performs a health check.
5. Opens the browser to the appropriate local URL.

---

# 28. STOP.BAT

Create a safe stop script.

It should stop only the services/processes belonging to this project where possible.

It should not blindly terminate unrelated Python processes.

---

# 29. UTILS.PY

Provide reusable utility functions for:

- paths
- subprocess execution
- command detection
- JSON loading
- JSON saving
- environment variables
- platform detection
- safe process handling
- formatting
- validation

---

# 30. CHAT MANAGER

`chat_manager.py` should provide an abstraction for:

```text
send message
stream response
select model
cancel response
conversation metadata
```

Use Ollama's supported API/interface.

Streaming should be supported where practical.

---

# 31. MODEL MANAGER

`model_manager.py` should provide:

```text
install_model()
remove_model()
list_models()
get_model_info()
select_model()
stop_model()
switch_model()
```

The manager must ensure the one-model-at-a-time policy.

---

# 32. OLLAMA MANAGER

`ollama_manager.py` should communicate with Ollama.

Support:

```text
GET /api/tags
POST /api/generate
POST /api/chat
POST /api/pull
POST /api/show
```

Use the current official Ollama API documentation when implementing.

Handle streaming correctly.

---

# 33. WEBUI MANAGER

`webui_manager.py` should:

- detect Open WebUI
- determine URL
- test connectivity
- provide configuration guidance
- optionally open it in a browser
- report connection problems

Do not attempt to impersonate Open WebUI.

---

# 34. TOOL MANAGER

`tool_manager.py` should maintain a controlled registry of available tools.

Example:

```text
web_search
document_search
calculator
code_execution
terminal
system_info
```

Tools must be explicitly enabled.

Dangerous tools must require approval.

---

# 35. DOCUMENT MANAGER

`document_manager.py` should handle:

```text
upload
validation
metadata
file type
size
storage
cleanup
```

Do not execute uploaded files automatically.

---

# 36. WEB SEARCH MANAGER

`web_search.py` should provide an abstraction over configured search providers.

Use:

```text
SEARCH_PROVIDER
SEARCH_API_KEY
```

from environment/configuration.

The system must continue functioning without web search.

---

# 37. CODE EXECUTOR

`code_executor.py` should safely handle code execution.

Prioritize:

```text
Python
```

Use isolation where practical.

Return:

```text
stdout
stderr
exit status
execution time
```

Do not execute code automatically unless the user has enabled the feature and the environment allows it.

---

# 38. TERMINAL MANAGER

`terminal_manager.py` should provide controlled command execution.

Implement approval mechanisms.

Never run terminal commands as Administrator by default.

Dangerous command patterns should trigger confirmation or rejection.

---

# 39. VOICE MANAGER

`voice_manager.py` should coordinate:

```text
recording
Whisper
LLM
TTS
playback
```

Keep each component optional.

---

# 40. WHISPER MANAGER

`whisper_manager.py` should:

- detect Whisper installation
- load Whisper only when needed
- transcribe audio
- return text
- handle model-not-found errors
- allow configuration of the Whisper model

---

# 41. TTS MANAGER

`tts_manager.py` should provide a common TTS interface.

Example:

```text
speak(text)
save_audio(text, path)
available_engines()
select_engine()
```

---

# 42. TAMIL TTS

`tamil_tts.py` should provide Tamil-specific TTS handling.

Support:

```text
AI4Bharat VITS-Rasa
```

and/or:

```text
facebook/mms-tts-tam
```

depending on availability.

Gracefully handle missing dependencies.

---

# 43. WEB LANDING PAGE

Create `index.html` as a professional landing page.

It should NOT pretend to be the official website of:

- Ollama
- DeepSeek
- Meta
- Google
- Microsoft
- Open WebUI
- GitHub
- AI4Bharat

Instead, describe this project as an independent local AI platform built using open-source technologies.

The landing page should visually communicate:

```text
LOCAL AI
PRIVATE
CPU FRIENDLY
8 GB RAM
OPEN SOURCE
MULTI-MODEL
CHATGPT-STYLE
```

Include sections:

### Hero

```text
Your Local AI Workspace
```

Explain that the platform brings lightweight local AI models together through Ollama and Open WebUI.

### Features

Include:

- Local chat
- Multiple models
- Model switching
- Coding assistant
- RAG
- Documents
- Web search
- Memory
- Voice input
- Tamil TTS
- Code execution
- Tools
- Privacy-focused local operation

### Models

Display the supported model list.

### Architecture

Show:

```text
User
 ↓
Open WebUI
 ↓
Local AI Controller
 ↓
Ollama
 ↓
Selected Model
```

### Technology

Include cards/links for:

```text
Ollama
Open WebUI
Llama
Gemma
Phi
Qwen
DeepSeek
Whisper
AI4Bharat
GitHub
```

Clearly identify each as a third-party project where applicable.

### Privacy

Explain that local inference can keep prompts/documents on the user's computer, but external services such as web search may transmit data depending on configuration.

### Footer

Include:

```text
Independent open-source project
Powered by open-source AI technologies
```

Do not use misleading official logos or trademarks without appropriate attribution.

---

# 44. README.MD

Create a professional README containing:

- Project title
- Description
- Features
- Supported hardware
- Supported models
- Architecture
- Installation
- Usage
- Model switching
- Voice
- RAG
- Web search
- Configuration
- Troubleshooting
- Security
- Privacy
- License
- Acknowledgements

---

# 45. LICENSE.MD

Use a suitable open-source license for the project's OWN source code.

If no license has been specified, use:

```text
MIT License
```

Clearly state that this license applies to this project and does NOT automatically relicense third-party software/models.

---

# 46. CODE_OF_CONDUCT.MD

Create a professional open-source Code of Conduct.

Include:

- expected behavior
- unacceptable behavior
- reporting process
- enforcement
- community standards

---

# 47. CONTRIBUTING.MD

Explain:

- how to fork
- create a branch
- make changes
- test
- document changes
- submit pull requests
- report issues

---

# 48. SECURITY.MD

Create a security policy covering:

- responsible vulnerability reporting
- secrets
- local API exposure
- terminal execution
- code execution
- uploaded documents
- web search
- network exposure
- authentication
- unsafe configurations

Explicitly warn users not to expose Ollama's local API publicly without understanding the security implications.

---

# 49. ACKNOWLEDGEMENTS / DOCUMENTATION FILES

The following documentation files must all be complete and useful:

```text
ACKNOWLEDGEMENTS.md
CHANGELOG.md
INFORMATION.md
SETUP_GUIDE.md
REQUIREMENTS.md
ARCHITECTURE.md
PROJECT_STRUCTURE.md
MODEL_GUIDE.md
TOOL_LICENSES.md
PRIVACY.md
TROUBLESHOOTING.md
FAQ.md
API.md
CONFIGURATION.md
PERFORMANCE.md
RESOURCE_USAGE.md
ROADMAP.md
```

Each must contain real project-specific documentation.

---

# 50. REQUIREMENTS.TXT

Keep Python dependencies as lightweight as possible.

Do NOT add huge unnecessary dependencies.

Use packages only when actually required.

Potential categories include:

```text
requests/httpx
psutil
python-dotenv
```

and only add:

```text
open-webui
whisper
torch
transformers
TTS
```

or similar packages if they are actually required by the chosen implementation.

Do not unnecessarily install multiple heavyweight AI frameworks.

If Whisper/TTS can be optional, make them optional.

Document optional dependencies separately in `REQUIREMENTS.md`.

---

# 51. CONFIGURATION EXAMPLE

`.env.example` should contain placeholders such as:

```text
OLLAMA_HOST=http://127.0.0.1:11434
OPEN_WEBUI_URL=http://127.0.0.1:8080

DEFAULT_MODEL=llama3.2:3b

CONTEXT_LENGTH=8192
TEMPERATURE=0.7
TOP_P=0.9
TOP_K=40
REPEAT_PENALTY=1.1

WEB_SEARCH_ENABLED=false
RAG_ENABLED=true
MEMORY_ENABLED=true
CODE_EXECUTION_ENABLED=false
TERMINAL_ENABLED=false
VOICE_ENABLED=false

WHISPER_MODEL=base

TTS_ENGINE=
SEARCH_PROVIDER=
SEARCH_API_KEY=
```

Never put a real secret in this file.

---

# 52. .GITIGNORE

Ignore:

```text
.env
venv/
.venv/
__pycache__/
*.pyc
logs/
cache/
data/
uploads/
models/
*.tmp
*.log
```

Do not accidentally ignore important source files.

---

# 53. PRIVACY

The privacy documentation must explain the difference between:

### Local operations

```text
Ollama
Local LLM
Local documents
Local RAG
Local Whisper
Local TTS
```

and external operations:

```text
Web Search
External APIs
Optional cloud services
```

Do not claim that the entire system is automatically private if the user enables external services.

---

# 54. PERFORMANCE

Document realistic expectations for:

```text
8 GB RAM
CPU-only
1.5B–3.8B models
```

Explain that speed depends heavily on:

- CPU generation
- number of CPU cores
- RAM speed
- context size
- quantization
- background applications
- disk speed
- model size

Recommend closing unnecessary applications while using larger models.

---

# 55. RESOURCE MANAGEMENT

Implement resource-aware behavior.

Before loading a model:

```text
Check available RAM
       ↓
Check currently loaded model
       ↓
Stop old model
       ↓
Load selected model
       ↓
Run inference
```

After inactivity, optionally unload the model.

Make automatic unloading configurable.

---

# 56. USER EXPERIENCE

The system should feel like a unified assistant rather than a collection of unrelated scripts.

Provide:

```text
Model selector
System status
Current model
RAM status
Voice status
Web search status
RAG status
```

Use clear terminal output.

Example:

```text
╔══════════════════════════════════════╗
║       LOCAL AI ASSISTANT             ║
╠══════════════════════════════════════╣
║ Ollama       : ONLINE                ║
║ Open WebUI   : ONLINE                ║
║ RAM          : 8 GB                  ║
║ Active Model : Qwen2.5-Coder 3B      ║
║ CPU Mode     : ENABLED               ║
╚══════════════════════════════════════╝
```

---

# 57. MAIN.PY

`main.py` should be the main CLI/controller entry point.

Provide commands similar to:

```text
python main.py status
python main.py models
python main.py install-model
python main.py switch-model
python main.py start
python main.py stop
python main.py health
python main.py config
```

Provide a helpful interactive mode if practical.

---

# 58. APP.PY

`app.py` should provide the local controller API/interface.

Use a lightweight Python web framework only if necessary.

Expose safe endpoints such as:

```text
GET  /health
GET  /status
GET  /models
POST /models/select
POST /chat
POST /models/stop
```

Do not expose dangerous terminal/code execution endpoints without authentication/authorization or explicit local-only safeguards.

Bind to:

```text
127.0.0.1
```

by default.

---

# 59. API DOCUMENTATION

`API.md` must document:

- endpoint
- method
- request
- response
- errors
- authentication
- local-only behavior
- examples

Do not expose secret values in examples.

---

# 60. MODEL DOWNLOAD MANAGEMENT

The setup process should allow:

```text
Install all models
```

or:

```text
Install only selected models
```

Because the user specifically wants all models installed, provide an option to install all supported models.

But remember:

```text
INSTALLED ≠ LOADED
```

All models may exist on disk while only one is active in RAM.

Clearly explain this.

---

# 61. MODEL SWITCHING UX

Provide a model menu:

```text
1. Llama 3.2 3B
2. Gemma 2 2B
3. Phi 3.5 3.8B
4. Qwen2.5-Coder 3B
5. DeepSeek-R1 1.5B
6. OpenELM 3B
7. Ministral 3B
8. SmolLM2 1.7B
```

Selecting one should:

```text
Stop current model
↓
Select requested model
↓
Verify model exists
↓
Start/use selected model
↓
Display status
```

---

# 62. DEFAULT PRESETS

Create sensible presets:

```text
GENERAL
→ Llama 3.2 3B

FAST
→ SmolLM2 1.7B

CODING
→ Qwen2.5-Coder 3B

REASONING
→ DeepSeek-R1 1.5B

LIGHT GENERAL
→ Gemma 2 2B

BALANCED
→ Ministral 3B
```

Allow the user to change these.

---

# 63. NO IMAGE / VIDEO GENERATION

Do not implement:

```text
Stable Diffusion
Flux
ComfyUI
video generation
image-generation APIs
```

The project is intentionally text/audio/document/tool focused.

The landing page should explicitly state:

```text
Image and video generation are intentionally excluded.
```

---

# 64. SAFETY

The assistant must not:

- execute destructive commands automatically
- expose credentials
- intentionally bypass security controls
- modify Windows security settings without approval
- download arbitrary executables from unknown sources
- expose local services publicly by default
- claim that generated code is automatically safe
- claim web information is current when web search is disabled

---

# 65. TESTING

Before completing the project, test:

```text
Python syntax
Configuration loading
Ollama detection
Model listing
Model switching
Model stopping
Health check
API startup
Setup scripts
Batch scripts
HTML validity
JSON validity
```

Where possible, test with Ollama installed.

If a component cannot be tested in the Jules environment because an external dependency is unavailable, implement graceful detection and document the limitation.

---

# 66. DOCUMENTATION QUALITY

Every documentation file must be written specifically for this project.

Do not fill documentation with generic placeholder text such as:

```text
TODO
Add information here
Coming soon
Lorem ipsum
```

If something is not implemented, clearly state:

```text
Not currently implemented
```

and explain the intended future approach in `ROADMAP.md`.

---

# 67. LICENSE OF TOOLS

`TOOL_LICENSES.md` must explain that this project may depend on third-party technologies, including where applicable:

```text
Ollama
Open WebUI
Llama
Gemma
Phi
Qwen
DeepSeek
OpenELM
Ministral
SmolLM
Whisper
AI4Bharat VITS
Facebook MMS
Python packages
```

Do not falsely claim ownership of third-party models or software.

For every third-party dependency, document:

```text
Name
Purpose
Official source
License where known
Whether the license applies to software/model/data
```

Tell Jules to verify current license information from authoritative/official sources before writing it.

---

# 68. ACKNOWLEDGEMENTS

Credit the open-source projects and model creators used by the project.

Include an explicit statement similar to:

```text
This project is an independent integration/orchestration project.
It is not an official Ollama, Open WebUI, Meta, Google, Microsoft,
DeepSeek, Qwen, AI4Bharat, or Hugging Face product.
```

---

# 69. CHANGELOG

Initialize:

```text
## Unreleased

### Added
- Initial local AI assistant architecture
- Ollama integration
- Open WebUI integration
- Model management
- Voice architecture
- Tamil TTS architecture
- Resource monitoring
- Windows setup scripts
```

Only document functionality actually implemented.

---

# 70. INFORMATION.MD

Explain:

- What the project is
- Why it exists
- How local AI works
- Ollama's role
- Open WebUI's role
- Why multiple small models are useful
- Why only one model should run at once
- CPU-only limitations
- RAM limitations
- Voice architecture
- RAG
- Web search
- Security
- Privacy

---

# 71. SETUP GUIDE

`SETUP_GUIDE.md` must provide a complete beginner-friendly process:

```text
1. Install/check Python
2. Install Ollama
3. Install Open WebUI
4. Run setup.bat
5. Pull models
6. Run health check
7. Start services
8. Open WebUI
9. Select a model
10. Test chat
11. Test coding
12. Test documents
13. Configure voice
14. Configure Tamil TTS
```

Also include recovery steps.

---

# 72. TROUBLESHOOTING

Include solutions for at least:

```text
Ollama not found
Ollama won't start
Model not found
Model is too slow
Out of memory
Open WebUI doesn't open
Port conflict
Python dependency failure
Whisper failure
TTS failure
Tamil voice unavailable
RAG failure
Web search failure
Code execution failure
Terminal permission error
```

---

# 73. FAQ

Answer practical questions such as:

```text
Can this run without a GPU?
Can all models be installed?
Can multiple models be installed but only one loaded?
Can it work offline?
Does web search require internet?
Can I use Tamil?
Can I upload PDFs?
Can I use it for coding?
Can I change models?
Can I disable memory?
Can I disable web search?
Can I disable terminal access?
Is my data automatically sent to the cloud?
```

---

# 74. ROADMAP

Provide future possibilities without pretending they currently exist.

Possible future additions:

```text
Better local embeddings
More languages
Improved voice pipeline
More model families
Plugin marketplace
Advanced agent workflows
Better model routing
Hardware acceleration
Mobile client
Remote LAN client
```

---

# 75. ARCHITECTURE DIAGRAM

Document the architecture using ASCII diagrams.

Example:

```text
                    USER
                     │
                     ▼
              ┌──────────────┐
              │  Open WebUI  │
              └──────┬───────┘
                     │
                     ▼
          ┌────────────────────┐
          │ Local AI Controller│
          └─────────┬──────────┘
                    │
                    ▼
               ┌─────────┐
               │ Ollama  │
               └────┬────┘
                    │
             ONE ACTIVE MODEL
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Llama       Qwen        DeepSeek
```

---

# 76. FINAL PROJECT VALIDATION

Before finishing:

### File validation

Verify exactly:

```text
49 files
```

exist and correspond to the specified structure.

### Code validation

Run syntax checks.

### Configuration validation

Ensure:

```text
.env.example
```

does not contain real credentials.

### Windows validation

Ensure:

```text
setup.bat
setup.ps1
start.bat
stop.bat
```

are syntactically valid.

### Python validation

Compile/check all Python files.

### Documentation validation

Ensure documentation matches actual implementation.

---

# 77. FINAL OUTPUT FROM JULES

After building the project, provide a concise final report containing:

```text
PROJECT CREATED
```

Then:

```text
Files created: 49
Python files: ...
Documentation files: ...
Models configured: 8
Voice models: 2 options
GPU required: NO
Target RAM: 8 GB
Operating system: Windows 10
LLMs simultaneously loaded: 1
Image generation: EXCLUDED
Video generation: EXCLUDED
```

Also report:

```text
Files successfully validated
Files requiring manual configuration
Dependencies requiring optional installation
Features that require external services
```

Do not claim something is fully working if it could not be tested.

---

# 78. FINAL QUALITY STANDARD

The result must feel like a serious open-source project rather than a collection of example scripts.

Priorities:

1. Reliability
2. Simplicity
3. Low RAM usage
4. CPU compatibility
5. Security
6. Clear documentation
7. Easy Windows installation
8. Modular architecture
9. Open WebUI compatibility
10. Ollama compatibility
11. Model switching
12. Local-first operation
13. Future extensibility

The system should be capable of acting as a **local ChatGPT-style workspace** for:

```text
Conversation
Programming
Reasoning
Documents
RAG
Web research
Memory
Voice input
Tamil speech
Code execution
Tools
Terminal workflows
System information
```

while intentionally excluding:

```text
Image generation
Video generation
```

Build the complete project now. Do not only generate an architecture or proposal. Create the actual files, actual code, actual documentation, setup scripts, configuration, and validation needed for the project.