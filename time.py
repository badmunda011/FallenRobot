import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler

#time zone
TIME_ZONE = pytz.timezone(time.TIME_ZONE)
scheduler = AsyncIOScheduler(timezone=TIME_ZONE)


TIME_ZONE = "Asia/Kolkata"
