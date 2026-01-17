import random
import asyncio
from pyrogram.types import InputMediaPhoto
from pyrogram.errors import PeerIdInvalid
from helpers import Emoji

def umur_bar(value: int) -> str:
    filled = int(value / 10)
    empty = 10 - filled
    return "🧬" * filled + "⚪" * empty

# ======== CEK UMUR =========
async def cekumur_cmd(client, message):
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

    msg = await message.reply(f"{em.proses}**Lagi ngitung umur {nama}...**")
    persen = random.randint(1, 100)
    for i in range(0, persen + 1, 10):
        bar = umur_bar(i)
        await msg.edit(f"{em.proses}**Menghitung umur...**\n{bar} {i}%")
        await asyncio.sleep(0.5)

    umur = random.randint(10, 80)
    zodiak = random.choice([
        "♈ Aries", "♉ Taurus", "♊ Gemini", "♋ Cancer",
        "♌ Leo", "♍ Virgo", "♎ Libra", "♏ Scorpio",
        "♐ Sagitarius", "♑ Capricorn", "♒ Aquarius", "♓ Pisces"
    ])
    sifat = random.choice([
        "baik tapi kek anjing", "bocil suka ngentot", "dewasa tapi goblok",
        "bijak tapi kek memek", "pendiam tapi sering ngewe", "suka maling", "paling anjing"
    ])

    hasil = f"""
<b>𖠇 ᴄᴇᴋ ᴜᴍᴜʀ {nama}</b>
<blockquote><b>╭─── ✮ ʜᴀsɪʟ ᴘᴇɴɢᴇᴄᴇᴋᴀɴ ✮ ───</b>
<b>┆✧ ᴜᴍᴜʀ ᴘᴇʀᴋɪʀᴀᴀɴ : {umur} tahun</b>
<b>┆✧ ᴢᴏᴅɪᴀᴋ : {zodiak}</b>
<b>┆✧ ᴛɪᴘᴇ ᴏʀᴀɴɢɴʏᴀ : {sifat}</b>
<b>┆✧ ᴋᴇᴀᴋᴜʀᴀᴛᴀɴ : {umur_bar(persen)} {persen}%</b>
<b>╰──────────────────────</b></blockquote>
<b>ɴᴇxᴛ ᴄᴇᴋ ᴜᴍᴜʀɴʏᴀ sɪᴀᴘᴀ ʟᴀɢɪ 🧠</b>
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
