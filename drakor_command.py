from pyrogram import Client, filters

# Data Drakor
drakor_list = [
    {"judul": "Crash Landing on You", "tahun": 2019, "genre": "Romance, Comedy", "rating": 9.1},
    {"judul": "Goblin", "tahun": 2016, "genre": "Fantasy, Romance", "rating": 9.0},
    {"judul": "Vincenzo", "tahun": 2021, "genre": "Action, Crime", "rating": 8.8},
    {"judul": "Itaewon Class", "tahun": 2020, "genre": "Drama, Business", "rating": 8.7},
    {"judul": "Reply 1988", "tahun": 2015, "genre": "Family, Comedy", "rating": 9.2},
    {"judul": "Descendants of the Sun", "tahun": 2016, "genre": "Romance, Action", "rating": 8.6},
    {"judul": "Hospital Playlist", "tahun": 2020, "genre": "Medical, Friendship", "rating": 9.0},
]


# Format tampilan
def format_drakor(d):
    return f"🎬 {d['judul']} ({d['tahun']})\n🎭 Genre: {d['genre']}\n⭐ Rating: {d['rating']}/10\n"


# Command utama: .drakor
@Client.on_message(filters.command("drakor", ".") & filters.me)
async def drakor_menu(client, message):
    text = "**📺 Daftar Drakor**\n\n"
    for d in drakor_list:
        text += format_drakor(d) + "\n"
    await message.edit(text)


# Command cari judul: .cdrakor judul
@Client.on_message(filters.command("cdrakor", ".") & filters.me)
async def cari_judul(client, message):
    if len(message.command) < 2:
        return await message.edit("❌ Contoh: `.cdrakor goblin`")

    keyword = " ".join(message.command[1:]).lower()
    hasil = [d for d in drakor_list if keyword in d["judul"].lower()]

    if hasil:
        text = "**🔍 Hasil Pencarian Judul:**\n\n"
        for d in hasil:
            text += format_drakor(d) + "\n"
        await message.edit(text)
    else:
        await message.edit(f"❌ Tidak ditemukan Drakor dengan judul mengandung: `{keyword}`")


# Command cari genre: .gdrakor genre
@Client.on_message(filters.command("gdrakor", ".") & filters.me)
async def cari_genre(client, message):
    if len(message.command) < 2:
        return await message.edit("❌ Contoh: `.gdrakor romance`")

    keyword = " ".join(message.command[1:]).lower()
    hasil = [d for d in drakor_list if keyword in d["genre"].lower()]

    if hasil:
        text = "**🎭 Hasil Pencarian Genre:**\n\n"
        for d in hasil:
            text += format_drakor(d) + "\n"
        await message.edit(text)
    else:
        await message.edit(f"❌ Tidak ditemukan Drakor dengan genre mengandung: `{keyword}`")
