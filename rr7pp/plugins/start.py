import time

from rr7pp import app as rr7pp

from pyrogram import filters
from pyrogram.types import Message




@rr7pp.bot.on_message(filters.command("start"))
async def send_response(_, m: Message):
	await m.reply("**- اهلا بك عزيزي المالك ارسل /help لمساعدتك**")



@rr7pp.bot.on_message(filters.new_chat_members & filters.group)
async def added_to_group_msg(_, m: Message):
	if m.new_chat_members[0].is_self:
		try:
			await rr7pp.bot.send_message(
				m.chat.id,
				"ارسل /help لمعرفه المميزات."
			)
		except Exception as e:
			await rr7pp.error(m, e)
	else:
		return
