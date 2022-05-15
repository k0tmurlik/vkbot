from io import BytesIO

from qrcode import make
from vkbottle.bot import Blueprint

from config import photo_uploader, http_client

bp = Blueprint("PhotoHandler")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text='qr <text>')
async def qr(ans, text):

    img = make(text)
    fp = BytesIO()

    img.save(fp, 'PNG')
    setattr(fp, "name", "image.png")

    await ans.answer(f'💥 Ваш QR-код:', attachment=await photo_uploader.upload(fp))


@bp.on.message(text=['котик', 'кот'])
async def cat(ans):

    data = await http_client.request_content("https://thiscatdoesnotexist.com/", "get")
    await ans.answer('🔥 Готово. Сохраняй!', attachment=await photo_uploader.upload(data))


@bp.on.message(text='скрин <text>')
async def screenhot_site(ans, text):

    photo = await http_client.request_content(
        f"https://api.screenshotmachine.com/?key=3f7ba3&url={text}&dimension=1024x768",
        "get"
    )

    await ans.answer('🔥 Готово. Сохраняй!', attachment=await photo_uploader.upload(photo))


@bp.on.message(text=["собака", "пёс", "dog"])
async def dog(ans):

    data = await http_client.request_content("https://place.dog/600/600", "get")
    await ans.answer('🔥 Готово. Сохраняй!', attachment=await photo_uploader.upload(data))


@bp.on.message(text=["лиса", "лис", "fox"])
async def fox(ans):

    data = (await http_client.request_json("https://randomfox.ca/floof/", "get"))["image"]
    photo = await http_client.request_content(data, "get")
    await ans.answer('🔥 Готово. Сохраняй!', attachment=await photo_uploader.upload(photo))
