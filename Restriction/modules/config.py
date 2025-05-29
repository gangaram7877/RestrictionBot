from os import getenv


API_ID = int(getenv("API_ID", "29773843"))
API_HASH = getenv("API_HASH", "8b40e91c29a00fecb905d6eb6aee2b3b")
BOT_TOKEN = getenv("BOT_TOKEN", "7893289543:AAHm1bmPvdUCFNpw3lTIm4ZlnKvFlQoqS0A")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6350117077").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ganeshchouhan7877:rdX15xt2odwLpXVEdj@cluster0.8r5un.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002448672568"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", ""))

