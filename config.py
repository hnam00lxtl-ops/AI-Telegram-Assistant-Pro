from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_NAME = os.getenv("BOT_NAME", "AI Assistant Pro")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")

MODEL = os.getenv("MODEL", "qwen3")

ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

DATABASE = os.getenv("DATABASE", "data/database.db")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

MAX_MEMORY = int(os.getenv("MAX_MEMORY", "30"))

LANGUAGE = os.getenv("LANGUAGE", "vi")
