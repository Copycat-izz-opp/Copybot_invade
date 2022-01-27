import os
from PIL import Image, ImageDraw, ImageFont
from hellbot import CMD_HELP
from hellbot.utils import admin_cmd

@hellbot.on(admin_cmd(pattern="write ?(.*)"))
async def writer(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    else:
        return await eod(e, "`Give Some Texts Too`")
    k = await eor(e, "`Processing...`")
    img = Image.open("resources/template.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("resources/assfont.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "hellbot.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
    await k.delete()

CMD_HELP.update({"write": ".write <text or reply to text>` It will write on a paper."
})
