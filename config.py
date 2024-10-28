# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23159366"))
API_HASH = getenv("API_HASH", "4623dd30dd1303bddb729eb0862262d9")
BOT_TOKEN = getenv("BOT_TOKEN", "7058637587:AAHILYqEOgW7fWN8QqEGDCm2YQWbI5ApZ3c")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5222155765").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://testbot:testbot@cluster0.7rzwxwx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1001917606160")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002023786492"))
