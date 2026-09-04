import os
from pathlib import Path
from utils import save_json_file, load_json_file
from logger import logger

UPLOAD_DIR = Path("uploads")

class DocumentManager:
    def __init__(self):
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    def save_uploaded_file(self, filename: str, content_bytes: bytes) -> str:
        safe_path = UPLOAD_DIR / filename
        try:
            with open(safe_path, "wb") as f:
                f.write(content_bytes)
            logger.info(f"Saved uploaded file to {safe_path}")
            return str(safe_path)
        except Exception as e:
            logger.error(f"Failed to save document: {e}")
            return ""

    def list_documents(self) -> list:
        return [f.name for f in UPLOAD_DIR.glob("*") if f.is_file()]

document_manager = DocumentManager()
