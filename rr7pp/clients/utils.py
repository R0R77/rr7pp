import time
import platform

import logging 
from config import Config
from telegraph import Telegraph
from rr7pp.pyrogramx.methods import Methods
from pyrogram import __version__ as pyro_version
from rr7pp.database import Database
from rr7pp.helpers import Helpers




class Utils(Methods, Config, Database, Helpers):
	# الإصدارات /

	userbot_version = "v.0.0.1"
	assistant_version = "v.0.0.1"
	python_version = str(platform.python_version())
	pyrogram_version = str(pyro_version)

	# المحتويات /

	CMD_HELP = {}

	# معلومات المطور /

	owner_name = "`MUHAMMAD`"
	owner_id = 5341314435
	owner_username = "@R0R77"

	# اخرى /

	Repo = "t.me/jmthon"
	StartTime = time.time()

	# debugging /

	logging.getLogger("pyrogram.syncer").setLevel(logging.CRITICAL)
	logging.getLogger("pyrogram").setLevel(logging.CRITICAL)
	
	logging.basicConfig(format="%(asctime)s %(message)s")
	log = logging.getLogger("———")

	# telegraph /

	telegraph = Telegraph()
	telegraph.create_account(short_name=Config.TL_NAME if Config.TL_NAME else "مستخدم جمثون")

