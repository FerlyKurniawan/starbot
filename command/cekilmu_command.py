import asyncio
import random

async def cekilmu_cmd(client, message):
    # Pesan awal
    m = await message.reply("📿 Lagi ngeraba aura kamu... sepertinya ada ilmu di dalam dirimu 😳")

    target_user = None
    target_username_arg = None

    # Ambil argumen username (kalau ada)
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
            await m.edit("⚠️ Username tidak ditemukan. Mengecek ilmumu sendiri aja deh...")
            await asyncio.sleep(1.5)
    else:
        target_user = message.from_user

    if not target_user:
        target_user = message.from_user

    nama_target = target_user.first_name
    username_target = target_user.username

    # Animasi
    animasi_langkah = [
        "🔮 Menyalakan dupa sakral...",
        "📖 Membuka kitab rahasia...",
        "👁️ Membaca energi spiritual...",
        "🌀 Menyerap aura di sekitar kamu...",
        "📜 Dapat hasilnya..."
    ]

    for step in animasi_langkah:
        await asyncio.sleep(1.3)
        await m.edit(step)

    # Jenis ilmu lucu
    daftar_ilmu = [
        "🐍 Ilmu Ular Tidur — bisa bangun cuma kalau lapar.",
        "💨 Ilmu Kentut Gaib — bisa teleport 5 meter pas kaget.",
        "🔥 Ilmu Api Adem — kelihatan panas, tapi adem di hati.",
        "💧 Ilmu Air Males — cuma ngikut arus hidup.",
        "🦅 Ilmu Elang Rebahan — tajam matanya, tapi jarang terbang.",
        "🌙 Ilmu Bayangan Malam — suka nongol pas listrik mati.",
        "🌸 Ilmu Harum Mistis — aura kamu bisa bikin bunga mekar sendiri.",
        "🧠 Ilmu Pikiran Kosong — meditasi terus sampe lupa tujuan.",
        "💎 Ilmu Permata Gaib — mahal, tapi nggak bisa dijual.",
        "🧤 Ilmu Sentuhan Dingin — pegang es batu, langsung cair."
    ]

    # Kekuatan dan kelemahan lucu
    daftar_kekuatan = [
        "bisa ngilang pas disuruh bayar utang.",
        "auranya bikin orang tenang dan ngantuk.",
        "bisa nyembuhin wifi lemot dengan doa.",
        "punya kemampuan bikin hujan cuma di hati.",
        "bisa bikin musuh bingung tanpa alasan.",
        "suaranya bisa ngusir nyamuk radius 2 meter.",
        "energinya stabil meski belum makan 2 hari.",
        "punya insting kuat buat nemu promo gratis ongkir.",
        "bisa tidur di mana aja, bahkan pas berdiri.",
        "punya kharisma yang bikin kucing nurut."
    ]

    daftar_kelemahan = [
        "lemah terhadap godaan diskon Shopee.",
        "langsung drop kalau lihat mantan bahagia.",
        "nggak tahan liat makanan gratis.",
        "auranya melemah kalau belum ngopi.",
        "jadi labil kalau sinyal hilang.",
        "nggak fokus kalo ada notifikasi TikTok.",
        "bisa ke-reset kalau bangun kesiangan.",
        "auranya ngambang kalau belum makan nasi.",
        "suka error pas denger lagu galau.",
        "kadang ilmunya hilang pas disuruh serius."
    ]

    hasil_ilmu = random.choice(daftar_ilmu)
    hasil_kekuatan = random.choice(daftar_kekuatan)
    hasil_kelemahan = random.choice(daftar_kelemahan)

    username_teks = f"\n📎 Username: @{username_target}" if username_target else ""

    teks_akhir = f"""
<blockquote>
📿 <b>HASIL CEK ILMU</b> 📿

👤 Nama: <b>{nama_target}</b>{username_teks}
🧙‍♂️ Ilmu Kamu: {hasil_ilmu}
⚡ Kekuatan: {hasil_kekuatan}
💤 Kelemahan: {hasil_kelemahan}

🌀 Tenang... semua orang punya ilmu uniknya sendiri 😌
</blockquote>
"""

    await m.edit(teks_akhir)
