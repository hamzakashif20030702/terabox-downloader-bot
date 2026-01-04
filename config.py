import os


# -----------------------------
# Helpers
# -----------------------------

def env(name: str, default=None, cast=str):
    value = os.getenv(name)
    if value is None:
        return default
    try:
        return cast(value)
    except Exception:
        return default


def env_list(name: str, default=None, sep=",", cast=int):
    value = os.getenv(name)
    if not value:
        return default or []
    return [cast(v.strip()) for v in value.split(sep) if v.strip()]


# -----------------------------
# Telegram
# -----------------------------

API_ID = env("API_ID", 0, int)
API_HASH = env("API_HASH", "")
BOT_TOKEN = env("BOT_TOKEN", "")

BOT_USERNAME = env("BOT_USERNAME", "")

PRIVATE_CHAT_ID = env("PRIVATE_CHAT_ID", 0, int)
ADMINS = env_list("ADMINS", default=[])


# -----------------------------
# Redis
# -----------------------------

HOST = env("HOST", "localhost")
PORT = env("PORT", 6379, int)
PASSWORD = env("PASSWORD", "")


# -----------------------------
# Auth / Cookies
# -----------------------------

COOKIE = env("COOKIE", "")


# -----------------------------
# Force Join
# -----------------------------

FORCE_LINK = env("FORCE_LINK", "")


# -----------------------------
# External APIs
# -----------------------------

PUBLIC_EARN_API = env("PUBLIC_EARN_API", "")


# -----------------------------
# Validation (optional but recommended)
# -----------------------------

if not API_ID or not API_HASH:
    raise RuntimeError("API_ID and API_HASH must be set in environment variables")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN must be set in environment variables")
