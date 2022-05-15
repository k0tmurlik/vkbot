from config import bot
from vkbottle import load_blueprints_from_package

for bp in load_blueprints_from_package("blueprints"):
    bp.load(bot)

bot.run_forever()
