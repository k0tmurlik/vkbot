from vkbottle.bot import Blueprint
from config import http_client

bp = Blueprint("Generators")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text="лицо")
async def crowd(_):

    data = (await http_client.request_text("https://randomall.ru/api/general/crowd", "post")).replace('"', "")
    return f"💡 Сгенерировал персонажа.\n>> {data}"


@bp.on.message(text="способность")
async def abilities(_):

    data = (await http_client.request_text("https://randomall.ru/api/general/abilities", "post")).replace('"', "")
    return f"💡 Сгенерировал способность.\n>> {data}"


@bp.on.message(text="рисование")
async def draw_idea(_):

    data = (await http_client.request_json("https://randomall.ru/api/custom/gens/278", "post"))["msg"]
    return f"💡 Подобрал идею для рисования.\n>> {data}"
