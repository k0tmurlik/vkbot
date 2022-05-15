import traceback

from vkbottle.bot import *
from vkbottle import *
from vkbottle.api import *
from vkbottle.dispatch.rules import *
from gtts import gTTS
from io import *

bp = Blueprint("voices")
bp.labeler.vbml_ignore_case = True

@bp.on.message(text=['!озвучь <msg>'])
async def audio(message: Message, msg):
    try:
        tts = gTTS(text=msg, lang="ru")
        fp = BytesIO()
        tts.write_to_fp(fp)
        audio_message = await audio_uploader.upload_audio_message(fp, message.peer_id)
        #audio_message = await AudioUploader(bp.api).upload(fp, message.peer_id)
        await message.answer(attachment=audio_message)
    except:
        text = f'Произошла ошибка при переводе текста в гс:\n' + traceback.format_exc()
        return(text)