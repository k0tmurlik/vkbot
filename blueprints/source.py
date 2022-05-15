from json import loads
from vkbottle.bot import Blueprint

from config import http_client

bp = Blueprint("Source")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text='курс')
async def course(_):

    result = loads(
        await http_client.request_text("https://www.cbr-xml-daily.ru/daily_json.js", "get")
    )["Valute"]

    return (
        "\n".join(
            [
                f"📙 {i['Name']}: {round(i['Value'], 2)}₽"
                for i in result.values()
            ]
        )
    )
