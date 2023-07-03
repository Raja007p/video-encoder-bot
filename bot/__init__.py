import os
from pyrogram import Client
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')

api_id = int(os.environ.get("API_ID" , "22453439"))
api_hash = os.environ.get("API_HASH" , "7c5b78a27321ebacbb8c16f0622a27af")
bot_token = os.environ.get("BOT_TOKEN" , "5909665130:AAHrhwhnTS1Yv4GwzDNX2e7lWmF_pyM-Qck")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS" , "6184029705").split()))

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
