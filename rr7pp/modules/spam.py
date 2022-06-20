import asyncio

from pyrogram.types import Message

from rr7pp import app, gen




app.CMD_HELP.update(
	{"التكرار" : (
		"التكرار",
		{
		"تكرار [عدد] [نص]" : "امر تكرار الرسائل عادي.", 
		"مكرر [عدد] [وقت] [نص]" : "امر تكرار بالوقت الءي انت تحدده يكزن بالثواني حيث يرسل كل رساله بينها وقت معين "
		}
		)
	}
)




@app.on_message(gen("تكرار", allow = ["sudo"]))
async def spam_handler(_, m: Message):
	try:
		reply = m.reply_to_message
		reply_to_id = reply.message_id if reply else None
		cmd = m.text.split(None, 2)

		if not reply and app.long(m) == 1:
			await app.send_edit(m, "- يجب عليك الرد على النص المراد تكراره او وضعه مع الامر.", text_type=["mono"], delme=4)

		elif not reply and app.long(m) > 1:
			await m.delete()
			times = int(cmd[1]) if cmd[1].isdigit() else 0
			spam_msg = cmd[2]
			for x in range(times):
				await app.send_message(
					m.chat.id, 
					spam_msg, 
					reply_to_message_id=reply_to_id
				)
				await asyncio.sleep(0.10)

		elif reply:
			await m.delete()
			times = int(cmd[1]) if cmd[1].isdigit() else 0
			spam_msg = reply.message_id
			for x in range(times):
				await app.copy_message(
					m.chat.id, 
					m.chat.id, 
					spam_msg
				)
	except Exception as e:
		await app.error(m, e)




@app.on_message(gen("مكرر", allow = ["sudo"]))
async def delayspam_handler(_, m: Message):
	try:
		reply = m.reply_to_message
		cmd = m.command

		if app.long(m) < 3:
			await app.send_edit(m, f"الاستخدام: `{app.MyPrefix()[0]}مكرر [عدد التكرار] [الوقت بالثواني] [الرسالة]`")

		elif app.long(m) > 2 and not reply:
			await m.delete()
			msg = m.text.split(None, 3)
			times = int(msg[1]) if msg[1].isdigit() else None
			sec = int(msg[2]) if msg[2].isdigit() else None
			text = msg[3]
			for x in range(times):
				await app.send_message(
					m.chat.id,
					text
				)
				await asyncio.sleep(sec)
		else:
			await app.send_edit(m,"استخدم الامر بشكل صريح؟ !")
	except Exception as e:
		await app.error(m, e)


