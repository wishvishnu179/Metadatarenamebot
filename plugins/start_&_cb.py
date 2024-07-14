from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from helper.database import db
from config import Config, Txt
import humanize
from time import sleep


@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):

    if message.from_user.id in Config.BANNED_USERS:
        await message.reply_text("**Sᴏʀʀʏ, Yᴏᴜ Aʀᴇ Bᴀɴɴᴇᴅ 🚫.**")
        return

    user = message.from_user
    await db.add_user(client, message)
    button = InlineKeyboardMarkup([
                [InlineKeyboardButton('♨️ Mᴀɪɴ Cʜᴀɴɴᴇʟ', url='https://t.me/TGCinemaworld'),
                InlineKeyboardButton('🔍 Mᴏᴠɪᴇs Bᴏᴛ', url='https://t.me/TGCinemaworldbot/start')],
                [InlineKeyboardButton('✌️ Aʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('🛠️ Hᴇʟᴘ', callback_data='help')],
                [InlineKeyboardButton("👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", url='https://t.me/Vishnudhfm14')]
            ])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)

    if not Config.STRING_SESSION:
        if file.file_size > 2000 * 1024 * 1024:
            return await message.reply_text("**Sᴏʀʀy Bʀᴏ Tʜɪꜱ Bᴏᴛ Dᴏᴇꜱɴ'ᴛ Sᴜᴩᴩᴏʀᴛ Uᴩʟᴏᴀᴅɪɴɢ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 2Gʙ**")

    try:
        text = f"""**__Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Mᴇ Tᴏ Dᴏ Wɪᴛʜ Tʜɪs Fɪʟᴇ.?__**\n\n**Fɪʟᴇ Nᴀᴍᴇ** :- `{filename}`\n\n**Fɪʟᴇ Sɪᴢᴇ** :- `{filesize}`"""
        buttons = [[InlineKeyboardButton("📝 Sᴛᴀʀᴛ Rᴇɴᴀᴍᴇ 📝", callback_data="rename")],
                   [InlineKeyboardButton("🚫 Cᴀɴᴄᴇʟ 🚫", callback_data="close")]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Mᴇ Tᴏ Dᴏ Wɪᴛʜ Tʜɪs Fɪʟᴇ.?__**\n\n**Fɪʟᴇ Nᴀᴍᴇ** :- `{filename}`\n\n**Fɪʟᴇ Sɪᴢᴇ** :- `{filesize}`"""
        buttons = [[InlineKeyboardButton("📝 Sᴛᴀʀᴛ Rᴇɴᴀᴍᴇ 📝", callback_data="rename")],
                   [InlineKeyboardButton("🚫 Cᴀɴᴄᴇʟ 🚫", callback_data="close")]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('♨️ Mᴀɪɴ Cʜᴀɴɴᴇʟ', url='https://t.me/TGCinemaworld'),
                InlineKeyboardButton('🔍 Mᴏᴠɪᴇs Bᴏᴛ', url='https://t.me/TGCinemaworldbot/start')],
                [InlineKeyboardButton('✌️ Aʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('🛠️ Hᴇʟᴘ', callback_data='help')],
                [InlineKeyboardButton("👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", url='https://t.me/Vishnudhfm14')]
            ])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🚫 Cʟᴏꜱᴇ", callback_data="close"),
                InlineKeyboardButton("⬅️ Bᴀᴄᴋ", callback_data="start")
            ]])
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🚫 Cʟᴏꜱᴇ", callback_data="close"),
                InlineKeyboardButton("⬅️ Bᴀᴄᴋ", callback_data="start")
            ]])
        )

    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()
