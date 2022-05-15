from vkbottle.bot import Blueprint

from tokens import MusicToken
from config import http_client

bp = Blueprint("AudioSearch")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text='поиск <text>')
async def audio_search(ans, text):

    result = await http_client.request_json(
        f"https://api.vk.com/method/audio.search?q={text}&count=10&access_token={MusicToken}&v=5.130",
        "post",
        headers={
            "User-Agent":
            'KateMobileAndroid/56 lite-460 (Android 4.4.2; SDK 19; x86; unknown Android SDK built for x86; en)'
        }
    )

    attachments = [
        f"audio{res['ads']['content_id']}"
        for res in result["response"]["items"]
    ]

    if not attachments:
        return f"❓ Не удалось музыку по вашему запросу."

    await ans.answer(
        f'🔎 Всего найдено {result["response"]["count"]:,} песен.\n👤 Первые несколько песен:',
        attachment=attachments
    )
