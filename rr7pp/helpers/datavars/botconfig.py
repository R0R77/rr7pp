from pyrogram.types import Message




BOTDV = [
	"BOT_NAME",
	"BOT_USERNAME",
	"BOT_ID",
	"BOT_BIO",
	"BOT_PIC"
	]


class BotConfig(object):
	def BotName(self):
		"""Get your bot name"""
		return self.getdv("BOT_NAME") or self.BOT_NAME or self.bot.name or None


	def BotUserName(self):
		"""Get your bot username"""
		return self.getdv("BOT_USERNAME") or self.BOT_USERNAME or self.bot.username or None


	def BotMention(self):
		"""Get bot mention"""
		return f"[{self.BotName()}](tg://user?id={self.BotId()})" if self.BotName() and self.BotId() else None  


	def BotId(self):
		"""Get your bots telegram id"""
		return self.getdv("BOT_ID") or self.BOT_ID or self.bot.id or None


	def BotBio(self, m: Message):
		"""Get your bots bio"""
		official = f"اهلا {m.from_user.mention} اسمي هو {self.BotName()} انا هو البوت المساعد الخاص بك يمكنني مساعدتك في العديد من الاشياء اضغط في الاسفل."  
		get_bio = self.getdv("BOT_BIO") or self.BOT_BIO or official or None
		return f"{get_bio}\n\n**النـوع: **"


	def BotPic(self):
		"""Get your bot pic url"""
		return self.getdv("BOT_PIC") or self.BOT_PIC or None
	
