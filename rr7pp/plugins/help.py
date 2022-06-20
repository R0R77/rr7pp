from pyrogram import filters

from pyrogram.types import (
	InlineKeyboardMarkup, 
	Message,
)

from rr7pp import app





settings = app.BuildKeyboard((["• الاعدادات •", "open-settings-dex"], ["• الاوامر •", "rr7pp-dex-2"]))
extra = app.BuildKeyboard((["• الاضافيات •", "open-extra-dex"], ["• الحالة •", "open-stats-dex"]))
about = app.BuildKeyboard(([["حول السورس", "open-about-dex"]]))
close = app.BuildKeyboard(([["اغلاق", "close-dex"]]))
approve = app.BuildKeyboard(([["السماح", "approve-user"]]))
global_command = app.BuildKeyboard(([["• اوامر المساعد •", "global-commands"]]))
home_back = app.BuildKeyboard((["القائمة الرئيسية", "close-dex"], ["رجوع", "open-start-dex"]))





# /start command for bot
@app.bot.on_message(filters.command("help"))
async def start(_, m: Message):
	if m.from_user:
		if m.from_user.id == app.id:
			# bot pic
			if app.BotPic().endswith(".jpg" or "png" or "jpeg"):
				info = await app.bot.send_photo(
					m.chat.id,
					app.BotPic(),
					app.BotBio(m),
					reply_markup=InlineKeyboardMarkup(
						[ settings, extra, about, close ]
					),
				)
			elif app.BotPic().endswith(".mp4" or ".gif"):
				info = await app.bot.send_photo(
					m.chat.id,
					app.BotPic(),
					app.BotBio(m),
					reply_markup=InlineKeyboardMarkup(
						[ settings, extra, about, close ]
					),
				)
			else:
				info = await app.bot.send_message(
					m.chat.id,
					app.BotBio(m),
					reply_markup=InlineKeyboardMarkup(
					[ settings, extra, about, close ]
					),
				)

		elif m.from_user.id != app.id:
			info = await app.bot.send_photo(
				m.chat.id,
				app.PIC,
                f"اهلا بك {m.from_user.mention} . هذا هو البوت الخاص بسورس جمثون يمكنك عرض مميزات البوت من الاسفل",
				reply_markup=InlineKeyboardMarkup(
					[global_command]
				),
			)
		app.message_ids.update({info.chat.id : info.message_id})
	else:
		return




