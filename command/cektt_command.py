import random
import asyncio
from pyrogram.errors import PeerIdInvalid
from helpers import Emoji

def tt_bar(value: int) -> str:
    filled = int(value / 10)
    empty = 10 - filled
    return "💗" * filled + "⚫" * empty

# ======== CEK TT =========
async def cektt_cmd(client, message):
    em = Emoji(client)
    await em.get()
    reply = message.reply_to_message

    if reply:
        target = reply.from_user
        nama = target.first_name
        user_id = target.id
    elif len(message.command) > 1:
        nama = message.text.split(" ", 1)[1]
        user_id = None
    else:
        return await message.reply(f"{em.gagal}**Kasih nama atau reply dulu bang.**")

    msg = await message.reply(f"{em.proses}**Lagi ngukur aura tt {nama} dulu bentar...**")
    persen = random.randint(1, 100)
    for i in range(0, persen + 1, 10):
        bar = tt_bar(i)
        await msg.edit(f"{em.proses}**Analisa bentuk dan energi...**\n{bar} {i}%")
        await asyncio.sleep(0.5)

    hasil = f"""
<b>💗 ᴄᴇᴋ ᴛᴛ {nama}</b>
<blockquote><b>╭─── ✮ ʜᴀsɪʟ ᴘᴇɴɢᴇᴄᴇᴋᴀɴ ✮ ───</b>
<b>┆✧ ᴛɪᴘᴇ ᴛᴛ : {random.choice(['kecil kayak nasi kfc', 'gede sebelah', 'kecil tapi bikin puas', 'proporsional sempurna', 'super lembut'])}</b>
<b>┆✧ ᴛᴇᴋsᴛᴜʀ : {random.choice(['halus banget', 'empuk sebelah', 'sedikit bikin sange', 'empuk alami', 'kenyal menggoda'])}</b>
<b>┆✧ ᴡᴀʀɴᴀ ᴀᴜʀᴀ : {random.choice(['merona cerah', 'putih', 'hitam anjing', 'pink alami', 'misterius gelap'])}</b>
<b>┆✧ ᴋᴇɴᴛᴀʟᴀɴ ᴇɴᴇʀɢɪ : {random.choice(['stabil banget', 'kadang aktif', 'melebur dengan ludah', 'nggak stabil', 'overpower parah'])}</b>
<b>┆✧ ᴋᴇᴀᴋᴜʀᴀᴛᴀɴ : {tt_bar(persen)} {persen}%</b>
<b>╰──────────────────────────</b></blockquote>
<b>ɴᴇxᴛ ᴄᴇᴋ ᴛᴛɴʏᴀ sɪᴀᴘᴀ ʟᴀɢɪ 💗</b>
"""

    if reply:
        try:
            async for p in client.get_chat_photos(user_id, limit=1):
                photo = p.file_id
                file = await client.download_media(photo)
                await msg.delete()
                await message.reply_photo(file, caption=hasil)
                return
        except Exception as e:
            print(f"**Gagal ambil foto profil:** {e}")
            pass

    await msg.edit(hasil)
