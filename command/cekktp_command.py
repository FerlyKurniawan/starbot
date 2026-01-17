import random
import asyncio
from pyrogram.types import InputMediaPhoto
from pyrogram.errors import PeerIdInvalid
from helpers import Emoji

def ktp_bar(value: int) -> str:
    filled = int(value / 10)
    empty = 10 - filled
    return "🪪" * filled + "⚪" * empty

# ======== CEK KTP =========
async def cekktp_cmd(client, message):
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
        return await message.reply(f"{em.gagal} Kasih nama atau reply dulu bang.")

    msg = await message.reply(f"{em.proses} Sedang mencari data KTP {nama}...")
    persen = random.randint(1, 100)
    for i in range(0, persen + 1, 10):
        bar = ktp_bar(i)
        await msg.edit(f"{em.proses} Mengecek database Dukcapil...\n{bar} {i}%")
        await asyncio.sleep(0.5)

    nik = "".join(str(random.randint(0, 9)) for _ in range(16))
    tempat = random.choice(["Jakarta", "Bandung", "Surabaya", "Medan", "Bekasi"])
    tgl = f"{random.randint(1,28):02d}-{random.randint(1,12):02d}-{random.randint(1970,2010)}"
    jenis = random.choice(["Laki-laki", "Perempuan"])
    alamat = random.choice([
        "Jl. Mawar No.10", "Jl. Melati No.3", "Komplek Perumahan A-12",
        "Kp. Baru RT01/RW02", "Perum Graha Indah Blok C"
    ])
    agama = random.choice(["Islam", "Kristen", "Katolik", "Hindu", "Budha"])
    pekerjaan = random.choice(["Pelajar", "Karyawan", "Wiraswasta", "Petani", "Tidak Bekerja"])
    status = random.choice(["Belum Kawin", "Kawin", "Janda/Duda"])

    hasil = f"""
<b>🪪 CEK KTP {nama}</b>
<blockquote><b>╭─── ✮ DATA PENDUDUK ✮ ───</b>
<b>┆✧ NIK : {nik}</b>
<b>┆✧ Nama : {nama}</b>
<b>┆✧ TTL : {tempat}, {tgl}</b>
<b>┆✧ Jenis Kelamin : {jenis}</b>
<b>┆✧ Alamat : {alamat}</b>
<b>┆✧ Agama : {agama}</b>
<b>┆✧ Pekerjaan : {pekerjaan}</b>
<b>┆✧ Status : {status}</b>
<b>┆✧ Akurasi Data : {ktp_bar(persen)} {persen}%</b>
<b>╰──────────────────────</b></blockquote>
<b>✅ Data berhasil ditemukan!</b>
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
