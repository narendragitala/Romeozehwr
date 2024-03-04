from os import getenv

API_ID = int(getenv("API_ID", "13335263"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5473771943").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/84870d6d89b893e59c5f0.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/RRomeo-RJ/Romeo-UserBot")
BRANCH = getenv("BRANCH", "main")
