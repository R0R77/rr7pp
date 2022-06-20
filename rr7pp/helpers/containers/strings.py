class Strings(object):
	def stat_string(self):
		return f"""

			**الأسم:** {self.UserName()}
			**{self.BotName()} الاصدار:** {self.assistant_version}
			**اصدار البايثون :** {self.python_version}
			**اصدار البايروجرام:** {self.pyrogram_version}
			**قاعده البيانات:** {self.db_status()}
			**الوقت:** {self.uptime()}
			**نبذة المستخدم:** {self.UserBio()}
			"""



	def closed_menu_string(self):
		return f"""
			اهلا بك في سورس جمثون
			سورس جمثون يساعدك في العديد من الاشياء ولديه العديد من المميزات
			• تم اغلاق القائمة
			"""
