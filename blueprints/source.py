from json import loads
from vkbottle.bot import Blueprint

from config import http_client

bp = Blueprint("Source")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text='ะบััั')
async def course(_):

    result = loads(
        await http_client.request_text("https://www.cbr-xml-daily.ru/daily_json.js", "get")
    )["Valute"]

    return (
        "\n".join(
            [
                f"๐ {i['Name']}: {round(i['Value'], 2)}โฝ"
                for i in result.values()
            ]
        )
    )
