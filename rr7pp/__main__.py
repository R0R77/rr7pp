import asyncio
from pyrogram import idle
from rr7pp.clients import app




loop = asyncio.get_event_loop()


async def start_assistant():
    if app.bot:
        print("يتم تفعيل المساعد.\n")
        await app.bot.start()
        print("تم تشغيل المساعد.\n")
    else:
        print(
            "لم يتم تنصيب المساعد يبدو ان التوكن الخاص بك غير صحيح\n"
        )


async def start_userbot():
    if app:
        print("جار تفعيل السورس.\n")
        await app.start()
        print("تم التفعيل بنجاح.\n")
    else:
        print("لم يتم تنصيب السورس يرجى التاكد من الفارات والمعلومات الخاصه بك ...")





async def start_bot():
	print("___________________________________. اهـلا بـك فـي جمـثون .___________________________________\n\n\n")
	print("جـار تـحميل المـساعد.\n\n")
	plugins = app.import_module("rr7pp/plugins/", exclude=app.NoLoad())
	print(f"\n\n{plugins} تم التـثبيت\n\n")
	print("جـار تحـميل السورس.\n\n")
	modules = app.import_module("rr7pp/modules/", exclude=app.NoLoad())
	print(f"\n\n{modules} تم التثـبيت\n\n")
	await start_assistant()
	await start_userbot()
	print("تم تنصيب سورس بايروجرام جمثوم بنجاح ارسل  .فحص للتاكد من السورس")
	await idle()




if __name__ == '__main__':
	loop.run_until_complete(start_bot())



