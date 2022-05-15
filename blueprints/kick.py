import re

from vkbottle.bot import Blueprint, Message
from vkbottle import VKAPIError

bp = Blueprint("kick")
bp.labeler.vbml_ignore_case = True

#===============[Проверка на админа]==================
async def check(message, id: int) -> bool:
    items = (await bp.api.messages.get_conversations_by_id(peer_ids=message.peer_id)).items
    if not items:
        return False
    chat_settings = items[0].chat_settings
    admins = [417583878]
    return id in admins

async def getid(pattern: str) -> int:
    if pattern.isdigit():
        return pattern
    elif "vk.com/" in pattern:
        uid = (await bp.api.users.get(user_ids=pattern.split("/")[-1]))[0]
        return uid.id
    elif "[id" in pattern:
        uid = pattern.split("|")[0]
        return uid.replace("[id", "")

#=========================[Кик]=========================       
@bp.on.chat_message(text=['Кик', 'Кик <member>', '/kick', '/kick <member>'])
async def kick_handler(message: Message, member=None):
	if not await check(message, id=message.from_id):
		return "⚠ У тебя нет доступа!"
	if member is None:
		await message.answer("⚠ Укажите пользователя...")
	else:
		try:
			member = re.findall(r"[0-9]+", member)[0]
			await bp.api.messages.remove_chat_user(message.chat_id, int(member))
			return "✅ Пока!"
		except VKAPIError[15]:
			return "⚠ Возможно данный юзер является админом в беседе, либо у меня нет прав админа."