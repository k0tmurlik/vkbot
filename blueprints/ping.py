import traceback

from vkbottle.bot import *
from vkbottle import *
from vkbottle.api import *
from vkbottle.dispatch.rules import *

bp = Blueprint("get_ping")
bp.labeler.vbml_ignore_case = True

#===================[ПИНГ]===================
@bp.on.message(text=['пинг', 'бот', 'чек'])
async def get_ping(message: Message):
    try:
        await message.answer('✅ Работаю стабильно.')
    except:
        text = f'Ошибка:\n' + traceback.format_exc()
        await message.answer(text)