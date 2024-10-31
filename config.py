from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

DB_NAME = "shizuDB"
MONGO_URL = getenv("MONGO_URL", None)
