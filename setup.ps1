param (
    [switch]$SkipModels,
    [switch]$CheckOnly
)

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " Local AI Assistant Setup Script for Windows 10 " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

# Check Python
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "[+] Python detected." -ForegroundColor Green
} else {
    Write-Host "[-] Python is not installed or not in PATH." -ForegroundColor Red
    exit 1
}

# Check Ollama
if (Get-Command ollama -ErrorAction SilentlyContinue) {
    Write-Host "[+] Ollama detected." -ForegroundColor Green
} else {
    Write-Host "[!] Ollama command not found. Please ensure Ollama for Windows is installed." -ForegroundColor Yellow
}

if ($CheckOnly) {
    Write-Host "[+] Health check completed." -ForegroundColor Green
    exit 0
}

# Install Python requirements
Write-Host "[*] Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Copy .env if not exists
if (-not (Test-Path .env)) {
    Copy-Item .env.example .env
    Write-Host "[+] Created .env from .env.example" -ForegroundColor Green
}

# Pull models if requested
if (-not $SkipModels) {
    Write-Host "[*] Pulling default recommended model (llama3.2:3b)..." -ForegroundColor Yellow
    ollama pull llama3.2:3b
}

Write-Host "[+] Setup finished successfully!" -ForegroundColor Green
