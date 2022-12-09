import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5804982110:AAEVWwWxZm2_Wk7QqM1JSY1AwZxPgdFU3tg")
    
    API_ID = int(os.environ.get("API_ID", 20462802))
    
    API_HASH = os.environ.get("dd98d5b8a57cf65d450b746a9c9052af")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "308378488"))

    SESSION_NAME = "bokepup_bot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://savidnet:<password>@cluster0.i3xipy0.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
