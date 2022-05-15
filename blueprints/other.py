from vkbottle.bot import Blueprint
from random import randint, choice

from config import http_client

bp = Blueprint("OtherCommands")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text="рандом <number:int> <number_two:int>")
async def bones(_, number, number_two):

    if number > number_two:
        return "📠 Введите числа так, чтобы первое число не было больше второго."

    return f"📠 Ваше рандомное число: {randint(number, number_two):,}"


@bp.on.message(text=["время", "дата"])
async def time_get(_):

    now = await http_client.request_text("https://isdayoff.ru/now", "get")
    return f"📆 {now}"


@bp.on.message(text="монетка")
async def coin(_):

    return f"✊ Вам выпало: {choice(['решка', 'орёл'])}"


@bp.on.message(text="год <year:int>")
async def isleap(_, year: int):

    result = "високосный" if year % 4 == 0 else "не високосный"
    return f"📙 Год {year} {result}"
