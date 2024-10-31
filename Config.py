from os import getenv

from pyrogram import filters
from dotenv import load_dotenv
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()

SUKH = "shizuDB"
TIME_ZONE = "Asia/Kolkata"
MONGO_URL = getenv("MONGO_URL", None)


#time zone
TIME_ZONE = pytz.timezone(Config.TIME_ZONE)
scheduler = AsyncIOScheduler(timezone=TIME_ZONE)

