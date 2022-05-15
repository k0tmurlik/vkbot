from vkbottle.bot import Blueprint
from config import http_client

bp = Blueprint("TextTools")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text="раскладка <text>")
async def layout(_, text):

    toeng_table = {
        '~': 'ё', '!': '!', '@': '"', '#': '№', '$': ';', '%': '%', '^': ':', '&': '?', 'q': 'й', '?': ',',
        'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '>': 'Ю',
        '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', '<': 'Б',
        'k': 'л', 'l': 'д', ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и',
        'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.', 'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К',
        'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ъ', 'A': 'Ф',
        'S': 'Ы', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', ':': 'Ж',
        '"': 'Э', '|': '/', 'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь'
    }

    torus_table = {v: k for k, v in toeng_table.items()}
    results = [
        ''.join([toeng_table.get(c, c) for c in text]),
        ''.join([torus_table.get(c, c) for c in text])
    ]

    if results[0] == text:
        return f'⌨ Раскладка изменена: {results[1]}'

    return f'⌨ Раскладка изменена: {results[0]}'


@bp.on.message(text='переведи <lang> <text>')
async def translate(_, lang, text):

    translate_text = await http_client.request_json(
        f"https://api.mymemory.translated.net/get?q={text}&langpair={lang}",
        "get"
    )

    return f'💡 {translate_text["responseData"]["translatedText"]}'


@bp.on.message(text=['сократи <url>', '/сократи <url>'])
async def short(_, url):

    short_link = await bp.api.utils.get_short_link(url=url)
    short_clck = await http_client.request_text("get", f"https://clck.ru/--?url={url}")

    return f"💡 Сократил твою ссылку:\n1. {short_link.short_url}\n2. {short_clck}"
