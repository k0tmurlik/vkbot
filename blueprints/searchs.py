from vkbottle.bot import Blueprint
from wikipedia import set_lang, summary
from youtubesearchpython import Search

from config import http_client

bp = Blueprint("SearchInfo")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text='вики <text>')
async def wikipedia_search(_, text):

    try:
        set_lang("ru")
        return f'🔍 Вот что получилось найти по запросу {text}:\n{summary(text)}'

    except:
        return f"🤨 Ничего не нашлось!"


@bp.on.message(text='погода <uid>')
async def weather(_, uid):

    response = await http_client.request_json(
        f"http://api.openweathermap.org/data/2.5/weather?q={uid}"
        "&lang=ru&appid=cdffd7f507a7cbc8c4cba574f41201c0",
        "get"
    )

    temp_max = response["main"]["temp_max"]
    temp_min = response["main"]["temp_min"]

    try:
        return (
            f'🌏 Погода в городе {response["name"]}:'
            f'\n• 📃 Описание: {response["weather"][0]["description"]}'
            f'\n• 📊 Температура: {round(response["main"]["temp"] - 273)}°C '
            f'(Мин {round(temp_min - 273)}°C, Макс: {round(temp_max - 273)}°C)'
            f'\n• 💦 Влажность: {response["main"]["humidity"]}%'
            f'\n• 🌤 Облачность: {response["clouds"]["all"]}%'
        )

    except:
        return f'🌎 Произошла ошибка.\n• Указанный вами город не найден.'


@bp.on.message(text=['ковид', 'коронавирус'])
async def covid_get(_):

    latest = (
        await http_client.request_json("https://coronavirus-tracker-api.herokuapp.com/v2/latest", "get")
    )["latest"]

    return (
        f"😷 Статистика о коронавирусе в мире:\n"
        f"Зафиксированно случаев: {latest['confirmed']:,}\n"
        f"Смертей: {latest['deaths']:,}\nВыздоровели: {latest['recovered']:,}"
    )


@bp.on.message(text="айпи <ip>")
async def get_ip(_, ip):

    result = await http_client.request_json(
        f"http://api.ipapi.com/{ip}?access_key=2ca3e35c4557cd2ad78568f350f5ea39&language=ru&output=json",
        "get"
    )

    return (
        f"✅ Вот что мне получилось найти по данному IP-адресу:\n\n"
        f"IP-адрес: {result['ip']}\n"
        f"Тип: {result['type']}\n"
        f"Континент: {result['continent_name']}\n\n"
        f"Код страны: {result['country_code']}\n"
        f"Страна: {result['country_name']} {result['location']['country_flag_emoji']}\n"
        f"Регион: {result['region_name']}\n"
        f"Местоположение в координатах: {result['latitude']}, {result['longitude']}\n\n"
        f"Индекс города: {result['zip']}\n"
        f"Телефонный код: {result['location']['calling_code']}"
    )


@bp.on.message(text='видео <text>')
async def video(_, text):

    videosSearch = Search(text, limit=1)
    response = videosSearch.result()
    viev_count = response['result'][0]['viewCount']['text'].replace('views', '')

    return (
        f"🔗 Ссылка на видео: {response['result'][0]['link']}\n⏱ Длинна видео: "
        f"{response['result'][0]['duration']}\n"
        f"🖼 Название канала: {response['result'][0]['channel']['name']}"
        f"\n🔥 Название видео: {response['result'][0]['title']}\n"
        f"🌍 Количество просмотров: {viev_count}"
    )
