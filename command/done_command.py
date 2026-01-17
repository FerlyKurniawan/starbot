from pyrogram import Client, filters
import datetime

@Client.on_message(filters.command(["done"], prefixes=[".", "/", "!"]))
async def done_cmd(client, message):
    # ambil waktu otomatis
    tanggal = datetime.datetime.now().strftime("%d %B %Y")

    # ambil argumen setelah perintah, misal: .done ubot 1 bulan 5000 DANA
    args = message.text.split(maxsplit=4)
    if len(args) < 5:
        return await message.reply(
            "❗ Format salah.\nGunakan format:\n\n`.done <barang> <nominal> <pembayaran> <promo(optional)>`\n\nContoh:\n`.done ubot 1 bulan 5000 DANA promo`"
        )

    barang = args[1]
    nominal = args[2]
    payment = args[3]
    promo = args[4] if len(args) >= 5 else "tidak ada promo"

    teks = f"""
⿻  ⌜ 𝗗𝗢𝗡𝗘 ⌟  ⿻
─────────────────
▧ 𝗡𝗼𝗺𝗶𝗻𝗮𝗹 : {nominal}
▧ 𝗣𝗮𝘆𝗺𝗲𝗻𝘁 : {payment.upper()}
▧ 𝗧𝗮𝗻𝗴𝗴𝗮𝗹 : {tanggal}
▧ 𝗕𝗮𝗿𝗮𝗻𝗴 : {barang}
▧ 𝗣𝗿𝗼𝗺𝗼 : {promo}
─────────────────
𝐂𝐎𝐍𝐓𝐀𝐂𝐓 : @dotzbaikk
─────────────────
"""

    await message.reply(teks)
