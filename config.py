from vkbottle.bot import Bot
from vkbottle.http import AiohttpClient
from vkbottle import PhotoMessageUploader

from tokens import TokenBot

http_client = AiohttpClient()
bot = Bot(TokenBot, task_each_event=True)
photo_uploader = PhotoMessageUploader(bot.api)
