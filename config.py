import os

if os.uname()[1] == "localhost":
    response = os.system("pip3 install -r requirements.txt --no-cache-dir")
    if response == 0:
        print("- تم بنجاح تثبيت جميع المكاتب")
    else:
        print("فشل في تنزيل المكاتب")

class Config(object):
#jmthon pyrogram userbot

    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    SESSION = os.getenv("SESSION")
    TEMP_DICT = os.getenv("TEMP_DICT", os.path.abspath(".") + "/downloads/")
    UPSTREAM_REPO = os.getenv(
        "UPSTREAM_REPO", "https://github.com/R0R77/rr7pp.git"
    )
    HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
    DB_URI = os.getenv("DATABASE_URL")
    SUDO_USERS = [
        int(x) for x in os.getenv("SUDO_USERS", "").split()
    ]
    LOG_CHAT = int(os.getenv("LOG_CHAT"))
    PREFIX = os.getenv("PREFIX", ".")
    WORKERS = int(os.getenv("WORKERS", 8))
    NO_LOAD = [int(x) for x in os.getenv("NO_LOAD", "").split()]
    AFK_TEXT = os.getenv("AFK_TEXT", "عذرا انا مشغول الان")
    PMPERMIT = os.getenv("PMPERMIT", False)
    PMPERMIT_PIC = os.getenv("PMPERMIT_PIC")
    PMPERMIT_TEXT = os.getenv(
        "PMPERMIT_TEXT",
        "◞هٛلا حِـبيہَ 🤍👋🏿◟\n━─━─━─━─━─━─━ٴ \n◞ يمَڪטּ ﭑڪَـﯠَڼ نَـايـمَ ﺂۄِ مَشِغوݪ 🕷 ˛\n\n◞ﭑتَࢪِك ࢪَسِـاࢦتَڪ ﯠَ ﺂنتَظࢪَ اݪـࢪَډ 🕷 ˛\n\n◞خِـݪـيڪَ ثَڪِيࢦ وَ ـلا تَـڪمِـࢪ࣪ 🕷 ˛\n\n◞ﭑذا شَفـتِـڪَ تكمَـز ࢪَاح ﺂݪـبَسـڪ 🕷 ˛\n\n━═━═━═━═━═━═━"
    )
    PM_LIMIT = int(os.getenv("PM_LIMIT", 4))
    TIME_ZONE = os.getenv("TIME_ZONE", "Asia/Baghdad")
    USER_NAME = os.getenv("USER_NAME")
    USER_BIO = os.getenv("USER_BIO")
    USER_PIC = os.getenv("USER_PIC", "")
    USER_ID = os.getenv("USER_ID")
    USER_USERNAME = os.getenv("USER_USERNAME")
    BOT_BIO = os.getenv("BOT_BIO")
    BOT_NAME = os.getenv("BOT_NAME", "jmthon")
    BOT_PIC = os.getenv("BOT_PIC", "https://telegra.ph/file/f4cd14b4e4da388041489.jpg")
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    BOT_ID = os.getenv("BOT_ID")
    TOKEN = os.getenv("TOKEN")
    THUMB_PIC = os.getenv("THUMB_PIC", "material/images/rr7pp.png")
    TL_NAME = os.getenv("TL_NAME")
    HELP_EMOJI = os.getenv("HELP_EMOJI")
