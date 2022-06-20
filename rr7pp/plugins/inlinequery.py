from pyrogram import filters

from pyrogram.enums import ParseMode

from pyrogram.types import (
	InlineKeyboardButton, 
	InlineKeyboardMarkup, 
	InlineQueryResultArticle, 
	InlineQueryResultPhoto, 
	InputTextMessageContent, 
	CallbackQuery, 
	Message,
)

from rr7pp import app




settings = app.BuildKeyboard((["• الاعدادات •", "open-settings-dex"], ["• الاوامر •", "rr7pp-dex-2"]))
extra = app.BuildKeyboard((["• الاضافيات •", "open-extra-dex"], ["• الحالة •", "open-stats-dex"]))
about = app.BuildKeyboard(([["حول المطور", "open-about-dex"]]))
close = app.BuildKeyboard(([["اغلاق", "close-dex"]]))
approve = app.BuildKeyboard(([["السماح", "approve-user"]]))
global_command = app.BuildKeyboard(([["• الاوامر العامة •", "global-commands"]]))
home_back = app.BuildKeyboard((["القائمة الرئيسية", "close-dex"], ["رجوع", "open-start-dex"]))






# via bot messages
@app.bot.on_inline_query(filters.user(app.id))
def inline_result(_, inline_query):
	query = inline_query.query
	if query.startswith("#p0e3r4m8i8t5"):
		inline_query.answer(
		results=[
			InlineQueryResultPhoto(
				photo_url=app.PmpermitPic(),
				title="نظام جمثون للحماية",
                description="هذا هو نظام حماية جمثون ، يساعدك على منع الاشخاص الذين يعملون تكرار في الخاص",
                caption=app.PmpermitText(),
				parse_mode=ParseMode.DEFAULT,
				reply_markup=InlineKeyboardMarkup([approve])
			)
			],
		cache_time=1
		)
	elif query.startswith("#t5r4o9nn6"):
		inline_query.answer(
		results=[
			InlineQueryResultPhoto(
				photo_url=app.BotPic(),
				title="حول جمثون",
                description="هذه قائمه مساعده جمثون.",
                caption="** هذا هو دليل المساعده الخاص بك لسورس جمثون",
				parse_mode=ParseMode.DEFAULT,
				reply_markup=InlineKeyboardMarkup([settings, extra, about, close])
			)
			],
		cache_time=1
		)
	elif query.startswith("#i2l8v3"):
		inline_query.answer(
		results=[
			InlineQueryResultPhoto(
				photo_url=app.ialive_pic(),
				title="فحص بالانلاين",
				description="هذه الامر شبيه بامر `.فحص`  لكن بصيغه الانيلان",
				caption=f"**-** {app.USER_BIO}\n\n**- المالك**: [{app.name}](https://t.me/{app.username})\n**- اصدار جمثون:** `{app.userbot_version}`\n**- اصدار البايثون:** `{app.python_version}`\n**- اصدار البايروجرام:** `{app.pyrogram_version}`\n**- الوقت:** `{app.uptime()}\n\n",
				parse_mode=ParseMode.DEFAULT,
				reply_markup=InlineKeyboardMarkup([home_back])
			)
			],
		cache_time=1
		)
	elif query.startswith("#q7o5e"):
		inline_query.answer(
		results=[
			InlineQueryResultArticle(
				title="الاقتباسات",
				input_message_content=InputTextMessageContent(app.quote()),
				description="**- من هنا يمكنك الحصول على اقتباسات شخصيات الانمي**",
				reply_markup=InlineKeyboardMarkup(
					[
						[
							InlineKeyboardButton(
								"عرض المزيد", callback_data="more-anime-quotes"
							)
						],
					]
				)
			)
		],
	cache_time=1
	)
