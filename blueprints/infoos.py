import time, platform, re
import os, sys
import traceback
import psutil, cpuinfo, uptime
import datetime
import math

from uptime import *
from io import *
from vkbottle.bot import Blueprint, Message

bp = Blueprint("InfoOS")
bp.labeler.vbml_ignore_case = True

#===============[Проверка на админа]==================
async def check(message, id: int) -> bool:
    items = (await bp.api.messages.get_conversations_by_id(peer_ids=message.peer_id)).items
    if not items:
        return False
    chat_settings = items[0].chat_settings
    admins = [417583878]
    return id in admins

#=========================[кмд]=========================       
@bp.on.message(text='инфа о системе')
async def infoos(message: Message):
    if not await check(message, id=message.from_id):
        return "⚠ У тебя нет доступа!"
    try:
        osname = os.uname().sysname 
    except:
        pass
    try:
        osarch = os.uname().machine
    except:
        pass
    try:
        osrelease = os.uname().release
    except:
        pass
    try:
        ospython = platform.python_version()
    except:
        pass
    try:
        diskused = psutil.disk_usage("/.").used / (1024 ** 3)
        disku = round(diskused, 1)
    except:
        pass
    try:
        disktotal = psutil.disk_usage("/.").total / (1024 ** 3)
        diskb = round(disktotal, 1)
    except:
        pass
    try:
        diskper = psutil.disk_usage("/.").percent
    except:
        pass
    try:
        time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d.%m.%Y %H:%M:%S")
    except:
        pass
    try:
        cpu = psutil.cpu_count(logical=True)
        loadcpu = psutil.cpu_percent(interval=1, percpu=True)
    except:
        pass
    try:
        useed_m = round(psutil.virtual_memory().used / 1024 ** 2)
        tot_m = round(psutil.virtual_memory().total / 1024 ** 2)
        used_m = round(useed_m, 2)
    except:
        pass
    try:
        inet_sent = psutil.net_io_counters().bytes_sent
        insent = int(inet_sent) / 100000 / 1024
        inet_recv = psutil.net_io_counters().bytes_recv
        inrecv = int(inet_recv) / 100000 / 1024 / 8
        inetsent = round(insent, 2)
        inetrecv = round(inrecv, 2)
    except:
        pass
    try:
        now = datetime.datetime.now()
        timeserv = now.strftime("%d.%m.%Y %H:%M:%S")
    except:
        pass
    try:
        upt = uptime() / 60 ** 2
        up = round(upt, 1)
    except:
        pass
    try:
        text = f'''
     ___________________________
     🖥Информация о системе:
     • OC: {osname}
     • Arch: {osarch}
     • Release: {osrelease}
     • Python: {ospython}
     ___________________________
    ⚙Информация о железе:
     • Процессор: {cpuinfo.get_cpu_info()["brand_raw"]}
     • Загрузка CPU: {loadcpu}% [{cpu}]
     • Диск: {disku}ГБ / {diskb}ГБ [{diskper}%]
     • RAM: {useed_m}МБ / {tot_m}МБ
     • Кол-во отправ. данных: {inetsent}ГБ
     • Кол-вo прин. данных: {inetrecv}ГБ
     • Время последнего рестарта:
     > {time}
     • Время работы сервера:
     > {up} ч.
     • Время на сервере:
     > {timeserv}
     ___________________________
     '''
        return(text)
    except:
        text = f'Произошла ошибка:\n' + traceback.format_exc()
        return(text)

@bp.on.message(text='инфа о чате')
async def commands(message: Message):
    if not await check(message, id=message.from_id):
        return "⚠ У тебя нет доступа!"
    if message.reply_message:
        await message.answer(
            f"Id чата: {message.peer_id}\nId из ответа: {message.reply_message.from_id}\nId сообщения: {message.conversation_message_id} или {message.id}\nId пользователя: {message.from_id}"
        )
    else:
        await message.answer(
            f"Id чата: {message.peer_id}\nId сообщения: {message.conversation_message_id} или {message.id}\nId отправителя: {message.from_id}"
        )