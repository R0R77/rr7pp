from pyrogram.types import CallbackQuery
from pyrogram.errors import MessageNotModified





class AlertUser(object):
	def alert_user(self, func):
		async def wrapper(_, cb: CallbackQuery):
			if cb.from_user and not (cb.from_user.id == self.id or cb.from_user.id in self.SudoUsers()):
				await cb.answer(
					f"ليست لديك صلاحيات الدخول هنا نصب جمثون من هنا @jmthon", 
					show_alert=True
				)
			else:
				try:
					await func(_, cb)
				except MessageNotModified:
					pass
		return wrapper
