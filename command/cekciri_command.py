import random
import asyncio
from pyrogram.types import InputMediaPhoto
from pyrogram.errors import PeerIdInvalid
from helpers import Emoji


def love_bar(value: int) -> str:
    filled = int(value / 10)
    empty = 10 - filled
    return "❤️" * filled + "🖤" * empty

# ======== CEK KONTOL =========
async def cekkntl_cmd(client, message):
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

    msg = await message.reply(f"{em.proses}**Sedang mengecek kontol {nama}...**")
    persen = random.randint(1, 100)
    for i in range(0, persen + 1, 10):
        bar = love_bar(i)
        await msg.edit(f"{em.proses}**Mengecek...**\n{bar} {i}%")
        await asyncio.sleep(0.5)

    hasil = f"""
<b>𖠇 ᴄᴇᴋ ᴋᴏɴᴛᴏʟ {nama}</b>
<blockquote><b>╭─── ✮ ʜᴀsɪʟ ᴄᴇᴋ ᴋᴏɴᴛᴏʟ ✮ ───</b>
<b>┆✧ ᴡᴀʀɴᴀ ᴋᴏɴᴛᴏʟ : {random.choice(['irenk', 'pink', 'rainbow', 'itam cok', 'kuning'])}</b>
<b>┆✧ ᴡᴀʀɴᴀ ᴊᴇᴍʙᴜᴛ : {random.choice(['irenk', 'pink', 'rainbow', 'itam cok', 'kuning'])}</b>
<b>┆✧ ᴜᴋᴜʀᴀɴ ᴋᴏɴᴛᴏʟ : {random.choice(['16 cm', '10 cm', '15 cm', '6 cm', '1 cm', '3 cm'])}</b>
<b>┆✧ ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {random.choice(['bengkok', 'lurus', 'panjang kecil', 'lebar', 'tumpul'])}</b>
<b>┆✧ ᴋᴇᴀᴋᴜʀᴀᴛᴀɴ : {love_bar(persen)} {persen}%</b>
<b>╰──────────────────────</b></blockquote>
<b>ɴᴇxᴛ ᴄᴇᴋ ᴋᴏɴᴛᴏʟɴʏᴀ sɪᴀᴘᴀ ʟᴀɢɪ.</b>
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

# ======== CEK MEMEK =========
async def cekmmk_cmd(client, message):
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
        return await message.reply(f"{em.gagal}**Kasih nama atau reply dulu mek.**")

    msg = await message.reply(f"{em.proses}**Sedang mengecek memek {nama}...**")
    persen = random.randint(1, 100)
    for i in range(0, persen + 1, 10):
        bar = love_bar(i)
        await msg.edit(f"{em.proses}**Mengecek...**\n{bar} {i}%")
        await asyncio.sleep(0.5)

    hasil = f"""
<b>𖠇 ᴄᴇᴋ ᴍᴇᴍᴇᴋ {nama}</b>
<blockquote><b>╭─── ✮ ʜᴀsɪʟ ᴄᴇᴋ ᴍᴇᴍᴇᴋ ✮ ───</b>
<b>┆✧ ᴡᴀʀɴᴀ ᴍᴇᴍᴇᴋ : {random.choice(['pink', 'rainbow', 'itam', 'kuning'])}</b>
<b>┆✧ ᴡᴀʀɴᴀ ᴊᴇᴍʙᴜᴛ : {random.choice(['irenk', 'pink', 'rainbow', 'itam cok'])}</b>
<b>┆✧ ᴜᴋᴜʀᴀɴ ʟᴏʙᴀɴɢ : {random.choice(['16 inc', '10 inc', '15 inc', '6 inc', '1 inc', '3 inc'])}</b>
<b>┆✧ ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {random.choice(['berjembut', 'dah jebol', 'bau trasi', 'berlendir', 'lebar itam'])}</b>
<b>┆✧ ᴋᴇᴀᴋᴜʀᴀᴛᴀɴ : {love_bar(persen)} {persen}%</b>
<b>╰──────────────────────</b></blockquote>
<b>ɴᴇxᴛ ᴄᴇᴋ ᴍᴇᴍᴇᴋɴʏᴀ sɪᴀᴘᴀ ʟᴀɢɪ.</b>
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

# ======== CEK SANGE =========
async def ceksange_cmd(client, message):
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
        return await message.reply(f"{em.gagal}**Kasih nama atau reply dulu mek.**")

    msg = await message.reply(f"{em.proses}**Sedang mengecek kadar sange {nama}...**")
    persen = random.randint(1, 100)
    for i in range(0, persen + 1, 10):
        bar = love_bar(i)
        await msg.edit(f"{em.proses}**Mengecek...**\n{bar} {i}%")
        await asyncio.sleep(0.5)

    feedback = random.choice([
        "Sange parah!", "Biasa aja, ngopi dulu.", "Udah siap coli.",
        "Gatel pengen ngocok.", "Sange level dewa.", "Coba mandi dulu bang."
    ])

    hasil = f"""
<b>𖠇 ᴄᴇᴋ sᴀɴɢᴇ {nama}</b>
<blockquote><b>╭─── ✮ ʜᴀsɪʟ ᴄᴇᴋ sᴀɴɢᴇ ✮ ───</b>
<b>┆✧ ɴᴀᴍᴀ : {nama}</b>
<b>┆✧ sᴀɴɢᴇ : {persen}%</b>
<b>┆✧ ᴋᴇᴀᴋᴜʀᴀᴛᴀɴ : {love_bar(persen)}</b>
<b>┆✧ ᴋᴇᴛᴇʀᴀɴɢᴀɴ : {feedback}</b>
<b>╰──────────────────────</b></blockquote>
<b>ɴᴇxᴛ ᴄᴇᴋ sᴀɴɢᴇ sɪᴀᴘᴀ ʟᴀɢɪ.</b>
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
            print(f"Gagal ambil foto profil: {e}")
            pass

    await msg.edit(hasil)


AGAMA_LIST = ["Islam", "Kristen", "Hindu", "Buddha", "Konghucu", "Ateis"]

# ======== CEK AGAMA =========
async def cekagama_cmd(client, message):
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
        return await message.reply(f"{em.gagal}**Kasih nama atau reply dulu mek.**")

    msg = await message.reply(f"{em.proses}**Sedang mengecek agama {nama}...**")
    persen = random.randint(1, 100)
    for i in range(0, persen + 1, 10):
        bar = love_bar(i)
        await msg.edit(f"{em.proses}**Mengecek...**\n{bar} {i}%")
        await asyncio.sleep(0.5)
        
    agama = random.choice(AGAMA_LIST)    
    hasil = f"""
<b>𖠇 HASIL DETEKSI AGAMA DARI {nama}</b>
<blockquote><b>╭─── ✮ ʜᴀsɪʟ ᴄᴇᴋ ᴀɢᴀᴍᴀ ✮ ───</b>
<b>├ ɴᴀᴍᴀ : {nama}</b>
<b>├ ᴀɢᴀᴍᴀ : {agama}</b>
<b>├ ᴋᴇᴀᴋᴜʀᴀᴛᴀɴ : {love_bar(persen)} {persen}%</b>
<b>├ sᴇʟᴀᴍᴀᴛ ʏᴀ ᴀɢᴀᴍᴀ ɴʏᴀ ᴄᴏᴄᴏᴋ ᴋᴏᴋ
<b>╰────────────────────────</b></blockquote>
<b>ɴᴏᴛᴇ ᴍᴀᴀғ ʏᴀ {nama} ᴄᴜᴍᴀ ʙᴇᴄᴀɴᴅᴀ ᴋᴏᴋ 😁</b>  
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
            print(f"Gagal ambil foto profil: {e}")
            pass

    await msg.edit(hasil)

# ======== CEK JODOH =========
async def cekjdh_cmd(client, message):
    em = Emoji(client)
    await em.get()

    if len(message.command) < 2:
        return await message.reply(f"{em.gagal}**Gunakan format: .cekjdh [nama pasangan]**")

    nama_pasangan = message.text.split(" ", 1)[1]
    msg = await message.reply(f"{em.proses}**Sedang mengecek kecocokan jodoh dengan {nama_pasangan}...**")
    
    persen = random.randint(1, 100)
    status = ""

    if persen < 30:
        status = "💔 Wah sepertinya kurang cocok..."
    elif persen < 70:
        status = "❤️ Lumayan cocok, bisa dicoba..."
    else:
        status = "💘 Wahh jodoh sejati nih!"


    for p in range(0, 101, 20):
        bar = "█" * (p // 5) + "░" * (20 - (p // 5))
        await msg.edit(
            f"🔮 Mengecek kecocokan jodoh...\n\n"
            f"{p}%\n[{bar}]"
        )
        await asyncio.sleep(1.5)


    hasil = f"""
<b>𖠇 ʜᴀsɪʟ ᴄᴇᴋ ᴊᴏᴅᴏʜ</b>
<blockquote><b>╭─── ✮ ʜᴀsɪʟ ᴊᴏᴅᴏʜ ✮ ───</b>
<b>┆✧ ᴋᴀᴍᴜ ᴅᴀɴ {nama_pasangan}</b>
<b>┆✧ ᴋᴇᴄᴏᴄᴏᴋᴀɴ : {persen}%</b>
<b>┆✧ sᴛᴀᴛᴜs : {status}</b>
<b>╰──────────────────────</b></blockquote>
<b>ɴᴇxᴛ ᴄᴇᴋ ᴊᴏᴅᴏʜ sɪᴀᴘᴀ ʟᴀɢɪ.</b>
"""
    await msg.edit(hasil)