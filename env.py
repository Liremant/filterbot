import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
FILTER_GROUP = int(os.getenv("FILTER_GROUP"))
ADMIN_GROUP = int(os.getenv("ADMIN_GROUP"))
_raw_ids = os.getenv("ADMINS_ID", "")
MOD_CHAT_IDS = [int(x) for x in _raw_ids.split(",") if x.strip().isdigit()]
