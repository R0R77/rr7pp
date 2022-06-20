import asyncio
from pyrogram import filters
from pyrogram.types import Message
from io import BytesIO, StringIO
from rr7pp import app, gen

@app.on_message(gen("اذاعة", allow = ["sudo"]))
async def brodcast(_, m: Message):
    if m.reply_to_message:
        msg = m.reply_to_message.text.markdown
    else:
        await m.reply_text("**-ييجب عليك الرد على الرسالة المراد عمل اذاعة لها**")
        return

    exmsg = await m.reply_text("- جـار الأذاعـة انتـظر قليـلا")
    err_str, done_broadcast = "", 0

    async for dialog in app.iter_dialogs():
          try:
                await app.send_message(dialog.chat.id, msg, disable_web_page_preview=True)
                done_broadcast += 1
                await asyncio.sleep(0.1)
          except Exception as e:
            await m.reply_text(f"**- تم بنجاح الاذاعة: {dialog.chat.id} من الدردشات \n- خطأ لـ {e}**")
