import heroku3

from pyrogram import filters

from pyrogram.types import (
	InlineKeyboardButton, 
	InlineKeyboardMarkup, 
	CallbackQuery, 
	Message,
)

from rr7pp import app





# buttons
settings = app.BuildKeyboard((["• الاعدادات •", "open-settings-dex"], ["• الاوامر •", "rr7pp-dex-2"]))
extra = app.BuildKeyboard((["• الاضافيات •", "open-extra-dex"], ["• الحالة •", "open-stats-dex"]))
about = app.BuildKeyboard(([["حول السورس", "open-about-dex"]]))
close = app.BuildKeyboard(([["اغلاق", "close-dex"]]))
approve = app.BuildKeyboard(([["السماح", "approve-user"]]))
global_command = app.BuildKeyboard(([["• اوامر المساعد •", "global-commands"]]))
home_back = app.BuildKeyboard((["القائمة الرئيسية", "close-dex"], ["رجوع", "open-start-dex"]))




# modules dex
@app.bot.on_callback_query(filters.regex("rr7pp-dex-2"))
@app.alert_user
async def modules(_, cb):
	btn = app.HelpDex(0, app.CMD_HELP, "helpme")
	await cb.edit_message_text(
		f"**النوع:** البوت \n\n**اوامر البوت:** `{len(app.CMD_HELP)}`",
		reply_markup=InlineKeyboardMarkup(btn),
	)


# next page
@app.bot.on_callback_query(filters.regex(pattern="helpme_next\((.+?)\)"))
@app.alert_user
async def give_next_page(_, cb):
	current_page_number = int(cb.matches[0].group(1))
	buttons = app.HelpDex(current_page_number + 1, app.CMD_HELP, "helpme")
	print(cb.matches[0])
	print(dir(cb.matches[0]))
	await cb.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


# previous page
@app.bot.on_callback_query(filters.regex(pattern="helpme_prev\((.+?)\)"))
@app.alert_user
async def give_old_page(_, cb):
	current_page_number = int(cb.matches[0].group(1))
	buttons = app.HelpDex(current_page_number - 1, app.CMD_HELP, "helpme")
	await cb.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


# back from modules dex to home
@app.bot.on_callback_query(filters.regex(pattern="backme_(.*)"))
@app.alert_user
async def get_back(_, cb):
	page_number = int(cb.matches[0].group(1))
	buttons = app.HelpDex(page_number, app.CMD_HELP, "helpme")
	text = f"**الأوامـر:** `{len(app.CMD_HELP)}`"
	await cb.edit_message_text(text, reply_markup=InlineKeyboardMarkup(buttons))


# modules plugin page information
@app.bot.on_callback_query(filters.regex(pattern="modulelist_(.*)"))
@app.alert_user
async def give_plugin_cmds(_, cb):
	plugin_name, page_number = cb.matches[0].group(1).split("|", 1)
	plugs = await app.data(plugin_name)
	help_string = f"**الأمر:** {plugin_name}\n\n" + "".join(plugs)
	await cb.edit_message_text(
		help_string,
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						text="رجوع",
						callback_data=f"backme_{page_number}",
					)
				]
			]
		),
		)


# list of helpdex
@app.bot.on_callback_query(filters.regex("open-stats-dex"))
@app.alert_user
async def _stats(_, cb):
	await cb.edit_message_text(
		text=app.stat_string(),
		reply_markup=InlineKeyboardMarkup([home_back]),
	)


# about info
@app.bot.on_callback_query(filters.regex("open-about-dex"))
@app.alert_user
async def _about(_, cb):
	await cb.edit_message_text(
		text=f"**[ معلـومات المـطور ]:**\n\n**الاسم:** {app.assistant_name}\n**الجنس:** {app.assistant_gender}\n**المعرف:** @R0R77\n\n**[ أصدارات الـسورس ]:**\n\n**البايثون:** {app.python_version}\n**البايروجرام:** {app.pyrogram_version}\n**المساعد:**  {app.assistant_version}",
		reply_markup=InlineKeyboardMarkup([home_back]),
	)


@app.bot.on_callback_query(filters.regex("public-commands"))
@app.alert_user
async def _public(_, cb):
	await cb.edit_message_text(
		text="**اوامر الأضايفه:** /start\n**الاستخدام:** للتاكد من حاله البوت شغال او لا.\n\n**الامر:** /help\n**الاستخدام:** لعرض اوامر البوت ارسله.\n\n**الامر:** /id\n**الاستخدام:** لأرسال الايدي الخاص بك او ايظي المجموعة.\n\n**الامر:** /quote\n**الاستخدام:** يقوم بأرسال اقتباسات شخصيات الانمي بشكل عشوائي مع زر للتحكم.\n\n**الامر:** /ping\n**الاستخدام:** لعرض سرعة البوت الخاصه بك .\n\n",
        reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"رجوع", callback_data="open-extra-dex",
					),
				]
			]
		),
	)


@app.bot.on_callback_query(filters.regex("open-extra-dex"))
@app.alert_user
async def _extra(_, cb):
	await cb.edit_message_text(
		text="**اوامر البوت المساعد من الاسفل:**",
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"• أوامـر المساعد •",
						callback_data="public-commands"
					)
				],
				[
					InlineKeyboardButton(
						"القائمة الرئيسية",
						callback_data="close-dex"
					),
					InlineKeyboardButton(
						"رجوع",
						callback_data="open-start-dex"
					)
				],
			]
		),
	)


@app.bot.on_callback_query(filters.regex("close-dex"))
@app.alert_user
async def _close(_, cb: CallbackQuery):
	await cb.edit_message_text(
		text=app.closed_menu_string(),
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"فتح", callback_data="open-start-dex",
					)
				],
				[
					InlineKeyboardButton(
						"اغلاق", callback_data="delete-dex",
					)
				]
			]
		),
	)


@app.bot.on_callback_query(filters.regex("open-settings-dex"))
@app.alert_user
async def _settings(_, cb):
	await cb.edit_message_text(
		text="**اعدادات السورس الخاصه بسورس جمثون من الاسفل:**",
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"اعادة تشغيل", callback_data="restart-rr7pp",
					),
				],
				[
					InlineKeyboardButton(
						"ايقاف السورس", callback_data="shutdown-rr7pp",
					)
				],
				[
					InlineKeyboardButton(
						"تحديث السورس", callback_data="update-rr7pp",
					)
				],
				home_back,
			]
		),
	)


@app.bot.on_callback_query(filters.regex("update-rr7pp"))
@app.alert_user
async def _update_callback(_, cb):
	pass


@app.bot.on_callback_query(filters.regex("open-start-dex"))
@app.alert_user
async def _start(_, cb):
	await cb.edit_message_text(
		text = "**اهلا بك هذا هو البوت الخاص بسورس جمثون يمكنك عرض مميزات البوت من الاسفل**",
		reply_markup=InlineKeyboardMarkup(
			[settings, extra, about, close]
		),
	)


@app.bot.on_callback_query(filters.regex("restart-rr7pp"))
@app.alert_user
async def _restart_rr7pp(_, cb):
	await cb.edit_message_text(
		text="**اضغط على زر التأكيد لعمل اعاده تشغيل للبوت**:",
		reply_markup=InlineKeyboardMarkup(
			[ 
				[
					InlineKeyboardButton(
						"تأكيد", callback_data="restart-core",
					),
				],
				[
					InlineKeyboardButton(
						"القائمة الرئيسية", callback_data="close-dex",
					),
					InlineKeyboardButton(
						"رجوع", callback_data="open-settings-dex"
					)
				],
			]
		),
	)


@app.bot.on_callback_query(filters.regex("restart-core"))
@app.alert_user
async def _restart_core(_, cb):
	await cb.edit_message_text(
		text="**جار اعادة التشغيل يرجى الانتظار  .  .  .**",
        reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						text="رجوع", callback_data=f"open-settings-dex"
					),
				],
			]
		),
	)
	access = heroku3.from_key(app.HEROKU_API_KEY)
	application = access.apps()[app.HEROKU_APP_NAME]
	restart = application.restart()
	if not restart:
		await cb.edit_message_text(
			"**فشل في اعادة تشغيل السورس**",
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton(
							text="رجوع", 
							callback_data=f"open-settings-dex"
						),
					],
				]
			),
		)
	else:
		await cb.edit_message_text(
			"**جار اعادة التشغيل انتظر من 2-3 دقائق بعدها سيتم تشغيل السورس مره اخرى**",
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton(
							text="رجوع", 
							callback_data=f"open-settings-dex"
						),
					],
				]
			),
		)


@app.bot.on_callback_query(filters.regex("shutdown-rr7pp"))
@app.alert_user
async def _shutdown_rr7pp(_, cb):
	await cb.edit_message_text(
		text="**اضغط على زر التأكيد لأيقاف تشغيل السورس**:",
		reply_markup=InlineKeyboardMarkup(
			[ 
				[
					InlineKeyboardButton(
						"تأكيد", 
						callback_data="shutdown-core",
					),
				],
				[
					InlineKeyboardButton(
						"القائمة الرئيسية", callback_data="close-dex",
					),
					InlineKeyboardButton(
						"رجوع", callback_data="open-settings-dex"
					)
				],
			]
		),
	)


@app.bot.on_callback_query(filters.regex("shutdown-core"))
@app.alert_user
async def _shutdown_core(_, cb):
	await cb.edit_message_text(
		text="**جار ايقاف السورس يرجى الانتظار قليلا**", 
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						text="رجوع", 
						callback_data=f"open-settings-dex"
					),
				],
			]
		),
	)
	access = heroku3.from_key(app.HEROKU_API_KEY)
	application = access.apps()[app.HEROKU_APP_NAME]
	if not application:
		await cb.edit_message_text(
			"**فشل في ايقاف السورس، اوقفه بنفسك يدويا من هيروكو",
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton(
							text="رجوع", 
							callback_data=f"open-settings-dex"
						),
					],
				]
			),
		)
	else:
		if application:
			application.process_formation()["worker"].scale(0)
			await cb.edit_message_text(
				"**تم ايقاف تشغيل سورس جمثون بنجاح اذا احتجت تشغيله شغله من هيروكو يدويا**",
				reply_markup=InlineKeyboardMarkup(
					[
						[
							InlineKeyboardButton(
								text="رجوع", 
								callback_data=f"open-settings-dex"
							),
						],
					]
				),
			)
		else:
			sys.exit(0)


@app.bot.on_callback_query(filters.regex("more-anime-quotes"))
async def _more_anime_quotes(_, cb):
	await cb.edit_message_text(
		app.quote(),
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"عرض المزيد", 
						callback_data="more-anime-quotes",
					),
				]
			]
		),
	)


@app.bot.on_callback_query(filters.regex("global-commands"))
async def _global_commands(_, cb):
	await cb.edit_message_text(
		text="**اوامـر المسـاعد:**\n\nالامر: /start \n**الاستخدام:** للتأكد اذا كان البوت شغال او لا\n\n**الامر:** /help\n**الاستخدام:** لعرض اوامر البوت.\n\n**الامر:** /quote\n**الاستخدام:** لعرض اقتباسات شخصيات انمي بشكل عشوائي يقوم بوضع زر لعرض المزيد كذلك.\n\n**الامر:** /ping\n**الاستخدام:** لعرض سرعه البوت.\n\n**الامر:** /id\n**الاستخدام:** لعرض ايدي المجموعه و المستخدم.",
        reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
							"رجوع", callback_data="back-to-info",
					),
				]
			]
		),
	)


@app.bot.on_callback_query(filters.regex("back-to-info"))
async def _back_to_info(_, cb):
    await cb.edit_message_text(
        f"اضغط في الاسفل لعرض اوامر البوت الخاصه بسورس جمثون.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• عرض الاوامر •",
                        callback_data="global-commands",
                    )
                ]
            ]
        ),
    )





