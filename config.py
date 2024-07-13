import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22276741"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7c5b1b6872522503f4d6e66bf61e9f24")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://porpanaiallinall:uAzYM9KNcTZTLaJv@cluster007.fqlpcwg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster007")
