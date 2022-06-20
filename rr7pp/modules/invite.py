from pyrogram import Client,errors
import re
from rr7pp import app

@app.on_message("me")
async def so(client,message):
    try:
        if message.text.count(".اضافة"):
            chat = message.text.split(".اضافة ")[1]
            to_chat = message.chat.id
            app.edit_message_text(message.chat.id, message.message_id, f"- جار التشغيل الان ....")
            s = app.get_chat_members(chat)
            fo = "\n".join(re.findall("\"id\": (.*?),", str(s))).splitlines()
            done = 0
            for someone in fo:
                app.add_chat_members(to_chat, someone, forward_limit=1)
                done += 1
            app.edit_message_text(message.chat.id, message.message_id, f"تم بنجاح اضافة : {done}")
    except AttributeError:
        pass
    except errors.exceptions.bad_request_400.PeerFlood:
        app.edit_message_text(message.chat.id,message.message_id,f"تم بنجاح اضافة : {done}\n والحساب قد توقف عن الاضافه الان")
