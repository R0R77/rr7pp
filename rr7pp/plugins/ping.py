from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from rr7pp import app as mhd



@mhd.bot.on_message(filters.command("ping"))
async def bot_ping(_, m: Message):
	if not m.chat.type in ["supergroup", "group"]:
		start = datetime.now()
		end = datetime.now()
		ms = (end - start).microseconds / 1000
		await mhd.bot.send_message(
			m.chat.id,
			f"**البنك**\n`{ms}`\n**الوقت**: `{mhd.uptime()}`"
		)
	elif m.chat.type in ["supergroup", "group"]:
		start = datetime.now()
		msg = await mhd.bot.send_message(
			m.chat.id,
			".  .  ."
		)
		end = datetime.now()
		ms = (end - start).microseconds / 1000
		await msg.edit(f"**البنك**\n`{ms}`\n**الوقت**: `{mhd.uptime()}`"
