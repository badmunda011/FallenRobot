from os import getenv
from pyrogram import filters
from dotenv import load_dotenv
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()

BAD = "Asia/Kolkata"


#time zone
BAD = pytz.timezone(time.BAD)
scheduler = AsyncIOScheduler(timezone=BAD)
