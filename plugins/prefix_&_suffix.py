from pyrogram import Client, filters, enums
from helper.database import db


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Gɪᴠᴇ Tʜᴇ Pʀᴇғɪx__\n\nExᴀᴍᴩʟᴇ :- `/set_prefix @TGCinemaworld`**")
    prefix = message.text.split(" ", 1)[1]
    SnowDev = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ ...**", reply_to_message_id=message.id)
    await db.set_prefix(message.from_user.id, prefix)
    await SnowDev.edit("__**✅ Pʀᴇꜰɪx Sᴀᴠᴇᴅ**__")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    SnowDev = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ ...**", reply_to_message_id=message.id)
    prefix = await db.get_prefix(message.from_user.id)
    if not prefix:
        return await SnowDev.edit("__**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Pʀᴇꜰɪx**__")
    await db.set_prefix(message.from_user.id, None)
    await SnowDev.edit("__**❌️ Pʀᴇꜰɪx Dᴇʟᴇᴛᴇᴅ**__")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    SnowDev = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ ...**", reply_to_message_id=message.id)
    prefix = await db.get_prefix(message.from_user.id)
    if prefix:
        await SnowDev.edit(f"**Yᴏᴜʀ Pʀᴇꜰɪx :-**\n\n`{prefix}`")
    else:
        await SnowDev.edit("__**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Pʀᴇꜰɪx**__")


# SUFFIX
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Gɪᴠᴇ Tʜᴇ Sᴜғғɪx__\n\nExᴀᴍᴩʟᴇ :- `/set_suffix @TGCinemaworld`**")
    suffix = message.text.split(" ", 1)[1]
    SnowDev = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ...**", reply_to_message_id=message.id)
    await db.set_suffix(message.from_user.id, suffix)
    await SnowDev.edit("__**✅ Sᴜꜰꜰɪx Sᴀᴠᴇᴅ**__")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    SnowDev = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ...**", reply_to_message_id=message.id)
    suffix = await db.get_suffix(message.from_user.id)
    if not suffix:
        return await SnowDev.edit("__**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Sᴜꜰꜰɪx**__")
    await db.set_suffix(message.from_user.id, None)
    await SnowDev.edit("__**❌️ Sᴜꜰꜰɪx Dᴇʟᴇᴛᴇᴅ**__")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_csuffix(client, message):

    SnowDev = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ...**", reply_to_message_id=message.id)
    suffix = await db.get_suffix(message.from_user.id)
    if suffix:
        await SnowDev.edit(f"**Yᴏᴜʀ Sᴜꜰꜰɪx:-**\n\n`{suffix}`**")
    else:
        await SnowDev.edit("__**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Sᴜꜰꜰɪx**__")
