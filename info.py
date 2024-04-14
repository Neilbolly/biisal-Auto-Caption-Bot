# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "2003585377"))
API_ID = int(getenv("API_ID", "28666617"))
API_HASH = str(getenv("API_HASH", "d39b74f34ac6f967b25d05037c53814a"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "6407978936:AAH6PB2MBRSCGZWO893PuHC6eXXZaKrwum0"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://Gustavo:IWdSRM75R0atDNhG@gusvato.zya2mso.mongodb.net/?retryWrites=true&w=majority",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='telegram.me/bisal_files'>{file_name} Telegram : @Bisal_Files\n\nForward the file before Downloading.</a></b>",
    )
)
