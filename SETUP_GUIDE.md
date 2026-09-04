# Setup Guide

Step-by-step guide to installing and running the Local AI Assistant Platform on Windows 10.

## Prerequisites
1. **Windows 10** (64-bit).
2. **Python 3.10+**: Download and install Python from python.org (Ensure "Add Python to PATH" is checked).
3. **Ollama for Windows**: Download from [ollama.com](https://ollama.com).

## Installation Steps
1. Clone or download this project repository.
2. Open a command prompt or PowerShell window in the project folder.
3. Run `setup.bat` (or `.\setup.ps1` in PowerShell).
4. The setup script verifies dependencies, creates `.env`, and installs required Python packages.

## Starting the Platform
Double-click `start.bat` or run:
```cmd
start.bat
```
This starts the local controller API and launches your browser to Open WebUI / local landing page.

## Stopping Services
To stop background processes safely:
```cmd
stop.bat
```
