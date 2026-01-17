import asyncio
import random

async def cekjembut_cmd(client, message):
    # Pesan awal
    m = await message.reply("🍑 Lagi ngintip kondisi jembut kamu...")

    target_user = None
    target_username_arg = None

    # Ambil argumen username (jika ada)
    parts = message.text.split()
    if len(parts) > 1:
        target_username_arg = parts[1].lstrip('@')

    # Tentukan target (reply / argumen / pengirim)
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    elif target_username_arg:
        try:
            target_user = await client.get_users(target_username_arg)
        except Exception:
            target_user = message.from_user
            await m.edit("⚠️ Pengguna dengan username tersebut tidak ditemukan. Mengecek jembut kamu sebagai gantinya...")
            await asyncio.sleep(1.5)
    else:
        target_user = message.from_user

    if not target_user:
        target_user = message.from_user

    # Ambil info target
    nama_target = target_user.first_name
    username_target = target_user.username

    # Animasi langkah
    animasi_langkah = [
        "🔍 Memeriksa tekstur...",
        "🧪 Mengukur kekencangan...",
        "🤣 Waduh, ada yang lucu nih...",
        "📜 Dapat hasilnya..."
    ]

    for step in animasi_langkah:
        await asyncio.sleep(1.3)
        await m.edit(step)

    # Fakta acak jembut
    hasil_jembut_fakta = [
        "🍑 Jembutmu kayak marshmallow, empuk banget 😭",
        "🔥 Jembutmu panas kayak oven, siap bakar! 🔥",
        "🌀 Jembutmu unik, berputar sendiri kayak tornado 🌪️",
        "🐧 Jembutmu imut kayak penguin kecil 🐧",
        "💨 Jembutmu berangin, kayak kipas alami 💨",
        "🎨 Jembutmu artistik, kayak lukisan abstrak 🖌️",
        "🪁 Jembutmu ringan, bisa terbang kalau ditiup 🪁",
        "🥳 Jembutmu party mode on, semua orang senyum 😆",
        "🐙 Jembutmu fleksibel kayak gurita 🐙",
        "💎 Jembutmu mahal, kayak permata langka 💎"
    ]

    hasil_acak = random.choice(hasil_jembut_fakta)

    username_teks = f"\n📎 Username: @{username_target}" if username_target else ""

    teks_akhir = f"""
<blockquote>
🤣 <b>Hasil Cek Jembut Kamu</b> 🤣

👤 Nama: <b>{nama_target}</b>{username_teks}
🍑 Fakta Jembut: {hasil_acak}

😆 Santai aja, ini cuma hiburan kocak~
</blockquote>
"""
    await m.edit(teks_akhir)
