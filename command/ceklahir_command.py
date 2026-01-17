import asyncio
import random

async def ceklahir_cmd(client, message):
    m = await message.reply("🍼 Lagi ngintip riwayat kelahiran kamu...")

    target_user = None
    target_username_arg = None
    
    parts = message.text.split()
    if len(parts) > 1:
        target_username_arg = parts[1].lstrip('@')
    
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    elif target_username_arg:
        try:
            target_user = await client.get_users(target_username_arg)
        except Exception:
            target_user = message.from_user
            await m.edit_text("⚠️ Pengguna dengan username tersebut tidak ditemukan. Mengecek kelahiran Anda sebagai gantinya.")
            await asyncio.sleep(1.5)
            
    else:
        target_user = message.from_user
        
    if not target_user:
         target_user = message.from_user
         
    nama_target = target_user.first_name
    username_target = target_user.username

    animasi_langkah = (
        "🔍 Menelusuri rumah sakit...",
        "🧠 Menggali ingatan masa bayi kamu...",
        "🤣 Waduh, datanya agak lucu nih...",
        "📜 Dapat hasilnya..."
    )
    
    for step in animasi_langkah:
        await asyncio.sleep(1.3)
        await m.edit_text(step)

    hasil_lahir_fakta = (
        "🗑️ Lahirmu di tempat sampah tapi langsung diangkat malaikat 😭",
        "🚽 Lahirmu nyemplung ke kloset, bidannya panik 💩",
        "🐔 Lahirmu disambut ayam tetangga 🐓",
        "🪣 Lahirmu di ember cucian, spontan banget 😭",
        "📦 Lahirmu dikira paket COD tapi gak ada ongkir 📦",
        "🐮 Lahirmu di kandang sapi, moooo 🐄",
        "🧻 Lahirmu diselimutin tisu warung 😭",
        "🐸 Lahirmu barengan kodok hujan pertama 🐸",
        "🎤 Lahirmu nangisnya nyanyi lagu dangdut 🎶",
        "🪳 Lahirmu disaksikan kecoa tua di dapur 😭"
    )

    hasil_acak = random.choice(hasil_lahir_fakta)
    
    username_teks = f"\n📎 Username: @{username_target}" if username_target else ""

    teks_akhir = f"""
🤣 Hasil Cek Lahir Kamu 🤣

👤 Nama: {nama_target}{username_teks}
📅 Fakta Kelahiran: {hasil_acak}

😆 Jangan marah ya, emang datanya lucu banget~
"""
    
    await m.edit_text(teks_akhir)
