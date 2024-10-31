class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 25742938
    API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"

    CASH_API_KEY = "SYQ6UMP8YFB9Y9UI"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://bdiavagy:S4u8iRR0XVfKS_DHVupAROfMyIE1ZGXN@tai.db.elephantsql.com/bdiavagy"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "DevilsHeavenMF"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7894953989:AAFrVlA7YCbnT0CGawKxkal2hSJEFllODpc"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "3RV16TWH8JT9"  # Get this value from https://timezonedb.com/api

    TIME_ZONE = "Asia/Kolkata"

    DB_NAME = "shizuDB"

    OWNER_ID = 7009601543  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
