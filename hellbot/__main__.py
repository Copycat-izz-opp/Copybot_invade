import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from hellbot import LOGS, bot, tbot
from hellbot.config import Config
from hellbot.utils import load_module
from hellbot.version import __hell__ as hellver
hl = Config.HANDLER
HELL_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/f8df934fc7420b5e98493.jpg"

# let's get the bot ready
async def hell_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"HELLBOT_SESSION - {str(e)}")
        sys.exit()


# hellbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Starting Copycat Bot 🔰")
            bot.loop.run_until_complete(hell_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 Copycat Startup Completed 🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "hellbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/The-HellBot/Extra"
# if Config.EXTRA == "True":
#     try:
#         os.system(f"git clone {extra_repo}")
#     except BaseException:
#         pass
#     LOGS.info("Installing Extra Plugins")
#     path = "hellbot/plugins/*.py"
#     files = glob.glob(path)
#     for name in files:
#         with open(name) as ex:
#             path2 = Path(ex.name)
#             shortname = path2.stem
#             load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your Copycat Bot Is Now Working ⚡")
LOGS.info(
    "Head to @Copycat_Userbot for Updates. Also join chat group to get help regarding to Copycat Bot."
)

# that's life...
async def hell_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                HELL_PIC,
                caption=f"#START \n\nDeployed ¢σρу¢αт вσт Successfully\n\n**¢σρу¢αт вσт - {hellver}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [¢σρу¢αт вσт Channel](t.me/COPYCAT_USERBOT) for Updates & [¢σρу¢αт вσт Chat](t.me/SESSION_GROUPS) for any query regarding ¢σρу¢αт вσт",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join Copycat Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Copycat_Userbot"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@SESSION_GROUPS"))
#    except BaseException:
#        pass


bot.loop.create_task(hell_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# ¢σρу¢αт вσт
