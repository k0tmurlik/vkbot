from vkbottle.bot import *
from vkbottle import *
from vkbottle.api import *
from vkbottle.dispatch.rules import *

bp = Blueprint("events")
bp.labeler.vbml_ignore_case = True

beseda_logs = 2000000002

@bp.on.raw_event(GroupEventType.GROUP_JOIN, dataclass=GroupTypes.GroupJoin)
async def group_join_handler(event: GroupTypes.GroupJoin):
    try:
        user = (await bp.api.users.get(user_ids=event.object.user_id))[0]
        await bp.api.messages.send(
            peer_id=event.object.user_id,
            message=f"{user.first_name}, спасибо за подписку! <3",
            random_id=0
        )
    except:
    	pass
    try:
        await bp.api.messages.send(
            peer_id=beseda_logs,
            message=f"🥰 | @id{event.object.user_id}({user.first_name} {user.last_name}) вступил в группу.",
            random_id=0
        )
    except VKAPIError[901]:
        pass

@bp.on.raw_event(GroupEventType.GROUP_LEAVE, dataclass=GroupTypes.GroupLeave)
async def group_leave_handler(event: GroupTypes.GroupLeave):
    try:
        user = (await bp.api.users.get(user_ids=event.object.user_id))[0]
        await bp.api.messages.send(
            peer_id=event.object.user_id,
            message=f"{user.first_name}, пока пока, надеюсь ты вернёшься к нам <3",
            random_id=0
        )
    except:
    	pass
    try:
        await bp.api.messages.send(
            peer_id=beseda_logs,
            message=f"💔 | @id{event.object.user_id}({user.first_name} {user.last_name}) вышел из группы.",
            random_id=0
        )
    except VKAPIError[901]:
        pass

@bp.on.raw_event(GroupEventType.USER_BLOCK, dataclass=GroupTypes.UserBlock)
async def group_block_handler(event: GroupTypes.UserBlock):
    try:
        user = (await bp.api.users.get(user_ids=event.object.user_id))[0]
        admin = (await bp.api.users.get(user_ids=event.object.admin_id))[0]
        #timestamp = int(event.object.unblock_date())
        #unblockdate = datetime.datetime.fromtimestamp(timestamp)
        #unblockdt = unblockdate.strftime('%d.%m.%Y %H:%M:%S')
        await bp.api.messages.send(
            peer_id=beseda_logs,
            message=f"🚫 | @id{event.object.user_id}({user.first_name} {user.last_name}) был добавлен в чёрный список.\nАдминистратор: @id{event.object.admin_id}({admin.first_name} {admin.last_name})\nПричина: {event.object.comment}",
            random_id=0
        )
    except VKAPIError[901]:
        pass

@bp.on.raw_event(GroupEventType.USER_UNBLOCK, dataclass=GroupTypes.UserUnblock)
async def group_unblock_handler(event: GroupTypes.UserUnblock):
    try:
        user = (await bp.api.users.get(user_ids=event.object.user_id))[0]
        admin = (await bp.api.users.get(user_ids=event.object.admin_id))[0]
        await bp.api.messages.send(
            peer_id=beseda_logs,
            message=f"🙈 | @id{event.object.user_id}({user.first_name} {user.last_name}) был разблокирован.\nАдминистратор: @id{event.object.admin_id}({admin.first_name} {admin.last_name})",
            random_id=0
        )
    except VKAPIError[901]:
        pass

@bp.on.raw_event(GroupEventType.MESSAGE_ALLOW, dataclass=GroupTypes.MessageAllow)
async def group_ma_handler(event: GroupTypes.MessageAllow):
    try:
        user = (await bp.api.users.get(user_ids=event.object.user_id))[0]
        await bp.api.messages.send(
            peer_id=beseda_logs,
            message=f"🤪 | @id{event.object.user_id}({user.first_name} {user.last_name}) разрешил отправлять ему сообщения.",
            random_id=0
        )
    except VKAPIError[901]:
        pass

@bp.on.raw_event(GroupEventType.MESSAGE_DENY, dataclass=GroupTypes.MessageDeny)
async def group_md_handler(event: GroupTypes.MessageDeny):
    try:
        user = (await bp.api.users.get(user_ids=event.object.user_id))[0]
        await bp.api.messages.send(
            peer_id=beseda_logs,
            message=f"🤔 | @id{event.object.user_id}({user.first_name} {user.last_name}) запретил отправлять ему сообщения.",
            random_id=0
        )
    except VKAPIError[901]:
        pass