import requests
import sys
import yt_dlp

# خدعة برمجية: إيهام النظام بأن youtube_dl هي نفسها yt_dlp
sys.modules["youtube_dl"] = yt_dlp
from pyrogram import Client as Bot
from pyrogram.session import Session
Session.TIME_OFFSET = 0
from VCPlayBot.config import API_HASH
from VCPlayBot.config import API_ID
from VCPlayBot.config import BG_IMAGE
from VCPlayBot.config import BOT_TOKEN
from VCPlayBot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="VCPlayBot.modules"),
)

bot.start()
run()
