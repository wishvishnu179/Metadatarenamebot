import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "28786884")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "e45e49071c6f1ce834201a5611e75b81")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6864648554:AAGf9vTENUxQCMOQSm9k0Re7_zA15Yt6gMI")  # ⚠️ Required

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://hackpok:hackpok@cluster0.vxzb3f3.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/d5e694c4e6e00f95a7c48.jpg")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '5807740619').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "TGCinemaworld") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002052274277"))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b><i>Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.</i></b>

<b>Bot Is Made By :</b> @Vishnudhfm14
"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 My Nᴀᴍᴇ : {}
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/Vishnudhfm14>Vɪsʜɴᴜ MB🤍</a>
├☃️ Fᴏᴜɴᴅᴇʀ Oꜰ : <a href=https://t.me/TGCinemaworld>Jᴏɪɴ Hᴇʀᴇ</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├🌀 Mʏ Sᴇʀᴠᴇʀ : <a href=https://dashboard.render.com>Rᴇɴᴅᴇʀ</a>
╰───────────────⍟ </b>"""

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴᴀɪʟ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ.


📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ: <code> /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration} </code>

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ \nAɴᴅ Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].
"""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

<b>☞ Fᴏʀ Exᴀᴍᴘʟᴇ :-</b>

◦ <code><b> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="𝙑𝙄𝙎𝙃𝙉𝙐👽@𝐓𝐆𝐂𝐢𝐧𝐞𝐦𝐚𝐰𝐨𝐫𝐥𝐝" -metadata author="𝙑𝙄𝙎𝙃𝙉𝙐👽@𝐓𝐆𝐂𝐢𝐧𝐞𝐦𝐚𝐰𝐨𝐫𝐥𝐝" -metadata:s:s title="Subs By :-𝐕𝐢𝐬𝐡𝐧𝐮 𝐌𝐁🤍" -metadata:s:a title="𝙑𝙄𝙎𝙃𝙉𝙐👽@𝐓𝐆𝐂𝐢𝐧𝐞𝐦𝐚𝐰𝐨𝐫𝐥𝐝" -metadata:s:v title="𝙑𝙄𝙎𝙃𝙉𝙐👽@𝐓𝐆𝐂𝐢𝐧𝐞𝐦𝐚𝐰𝐨𝐫𝐥𝐝" </code>

<b><i>📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Vishnudhfm14</b></i>
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ Pʀᴏɢʀᴇss Bᴀʀ ❱━➣
┣⪼ 📁 Sɪᴢᴇ : {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ : {3}/s
┣⪼ ⏰️ Eᴛᴀ : {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `wishvishnu179-1@okaxis`
"""
