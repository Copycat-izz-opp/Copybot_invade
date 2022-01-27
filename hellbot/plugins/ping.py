import time
import asyncio
from datetime import datetime
from . import *

def up_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@bot.on(admin_cmd(pattern="ping$"))
async def ping(event):
      await event.edit("`·.·★ ℘ıŋɠ ★·.·´")
      x = await bot.get_me()
      name = x.first_name 
      idd = x.id
      mention = f"[{name}](tg://user?id={idd})"
      StartTime = time.time()
      uptime = up_time(time.time() - StartTime)
      start = datetime.datetime.now()
      end = datetime.datetime.now()
      speed = (end - start).microseconds / 1000
      await event.edit(f"""**╰•★ఌ︎  ℘ꨄ︎ŋɠ  ఌ︎★•╯**
   
    __ʂ℘ɛɛɖ :__ `{speed}`
    __ơῳŋɛཞ :__ {mention}
""")
