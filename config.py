from os import getenv
from pyrogram import filters
from dotenv import load_dotenv
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()

SUKH = "shizuDB"
BAD = "Asia/Kolkata"
MONGO_URL = getenv("MONGO_URL", None)


#time zone
BAD = pytz.timezone(time.BAD)
scheduler = AsyncIOScheduler(timezone=BAD)

