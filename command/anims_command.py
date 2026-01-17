import asyncio
import random
from pyrogram.errors import FloodWait
from time import sleep

from helpers import Quotly, Emoji, Message

DEFAULTUSER = "Dotz"


NOBLE = [
    "╲╲╲┏━━┓╭━━━╮╱╱╱\n╲╲╲┗┓┏┛┃╭━╮┃╱╱╱\n╲╲╲╲┃┃┏┫┃╭┻┻┓╱╱\n╱╱╱┏╯╰╯┃╰┫┏━╯╱╱\n╱╱┏┻━┳┳┻━┫┗┓╱╱╱\n╱╱╰━┓┃┃╲┏┫┏┛╲╲╲\n╱╱╱╱┃╰╯╲┃┃┗━╮╲╲\n╱╱╱╱╰━━━╯╰━━┛╲╲",
    "┏━╮\n┃▔┃▂▂┏━━┓┏━┳━━━┓\n┃▂┣━━┻━╮┃┃▂┃▂┏━╯\n┃▔┃▔╭╮▔┃┃┃▔┃▔┗━┓\n┃▂┃▂╰╯▂┃┗╯▂┃▂▂▂┃\n┃▔┗━━━╮┃▔▔▔┃▔┏━╯\n┃▂▂▂▂▂┣╯▂▂▂┃▂┗━╮\n┗━━━━━┻━━━━┻━━━┛",
    "┏┓┏━┳━┳━┳━┓\n┃┗┫╋┣┓┃┏┫┻┫\n┗━┻━┛┗━┛┗━┛\n────­­­­­­­­­YOU────",
    "╦──╔╗─╗╔─╔ ─\n║──║║─║║─╠ ─\n╚═─╚╝─╚╝─╚ ─\n╦─╦─╔╗─╦╦   \n╚╦╝─║║─║║ \n─╩──╚╝─╚╝",
    "╔══╗....<3 \n╚╗╔╝..('\\../') \n╔╝╚╗..( •.• ) \n╚══╝..(,,)(,,) \n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "░I░L░O░V░E░Y░O░U░",
    "┈┈╭━╱▔▔▔▔╲━╮┈┈┈\n┈┈╰╱╭▅╮╭▅╮╲╯┈┈┈\n╳┈┈▏╰┈▅▅┈╯▕┈┈┈┈\n┈┈┈╲┈╰━━╯┈╱┈┈╳┈\n┈┈┈╱╱▔╲╱▔╲╲┈┈┈┈\n┈╭━╮▔▏┊┊▕▔╭━╮┈╳\n┈┃┊┣▔╲┊┊╱▔┫┊┃┈┈\n┈╰━━━━╲╱━━━━╯┈╳",
    "╔ღ═╗╔╗\n╚╗╔╝║║ღ═╦╦╦═ღ\n╔╝╚╗ღ╚╣║║║║╠╣\n╚═ღ╝╚═╩═╩ღ╩═╝",
    "╔══╗ \n╚╗╔╝ \n╔╝(¯'v'¯) \n╚══'.¸./\n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "╔╗ \n║║╔═╦═╦═╦═╗ ╔╦╗ \n║╚╣╬╠╗║╔╣╩╣ ║║║ \n╚═╩═╝╚═╝╚═╝ ╚═╝ \n╔═╗ \n║═╬═╦╦╦═╦═╦═╦═╦═╗ \n║╔╣╬║╔╣╩╬╗║╔╣╩╣╔╝ \n╚╝╚═╩╝╚═╝╚═╝╚═╩╝",
    "╔══╗ \n╚╗╔╝ \n╔╝╚╗ \n╚══╝ \n╔╗ \n║║╔═╦╦╦═╗ \n║╚╣║║║║╚╣ \n╚═╩═╩═╩═╝ \n╔╗╔╗ ♥️ \n║╚╝╠═╦╦╗ \n╚╗╔╣║║║║ \n═╚╝╚═╩═╝",
    "╔══╗╔╗  ♡ \n╚╗╔╝║║╔═╦╦╦╔╗ \n╔╝╚╗║╚╣║║║║╔╣ \n╚══╝╚═╩═╩═╩═╝\n­­­─────­­­­­­­­­YOU─────",
    "╭╮╭╮╮╭╮╮╭╮╮╭╮╮ \n┃┃╰╮╯╰╮╯╰╮╯╰╮╯ \n┃┃╭┳━━┳━╮╭━┳━━╮ \n┃┃┃┃╭╮┣╮┃┃╭┫╭╮┃ \n┃╰╯┃╰╯┃┃╰╯┃┃╰┻┻╮ \n╰━━┻━━╯╰━━╯╰━━━╯",
    "┊┊╭━╮┊┊┊┊┊┊┊┊┊┊┊ \n━━╋━╯┊┊┊┊┊┊┊┊┊┊┊ \n┊┊┃┊╭━┳╮╭┓┊╭╮╭━╮ \n╭━╋━╋━╯┣╯┃┊┃╰╋━╯ \n╰━╯┊╰━━╯┊╰━┛┊╰━━",
]

SLEEP = 1


import asyncio

async def dotz(client, message):
    typew = await message.edit("RESTART DOTZ...")
    await asyncio.sleep(1)

    frames = [
        "`.`",
        "`D.`",
        "`DO.`",
        "`DOT.`",
        "`DOTZ.`",
        "```\n"
        "██████╗  ██████╗ ████████╗███████╗\n"
        "██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝\n"
        "██║  ██║██║   ██║   ██║   █████╗  \n"
        "██║  ██║██║   ██║   ██║   ██╔══╝  \n"
        "██████╔╝╚██████╔╝   ██║   ███████╗\n"
        "╚═════╝  ╚═════╝    ╚═╝   ╚══════╝\n"
        "```",
        "```\n"
        "██████╗  ██████╗ ████████╗███████╗\n"
        "██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝\n"
        "██║  ██║██║   ██║   ██║   █████╗  \n"
        "██║  ██║██║   ██║   ██║   ██╔══╝  \n"
        "██████╔╝╚██████╔╝   ██║   ███████╗\n"
        "╚═════╝  ╚═════╝    ╚═╝   ╚══════╝\n\n"
        "       [ POWERED BY DOTZ TEAM ⚡ ]\n"
        "```",
        "`DOTZ siap melayani dengan kecepatan maksimal! ⚡`",
        "`Belanja followers, kuota, dan pulsa? Cuma di DOTZ PEDIA! 💥`",
        "```\n"
        "██████╗  ██████╗ ████████╗███████╗\n"
        "██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝\n"
        "██║  ██║██║   ██║   ██║   █████╗  \n"
        "██║  ██║██║   ██║   ██║   ██╔══╝  \n"
        "██████╔╝╚██████╔╝   ██║   ███████╗\n"
        "╚═════╝  ╚═════╝    ╚═╝   ╚══════╝\n"
        "```"
    ]
    
    for frame in frames:
        await typew.edit(frame)
        await asyncio.sleep(1.2)


async def robot(client, message):
    typew = await message.edit("🔧 Mengaktifkan DOTZ ROBOT...")
    await asyncio.sleep(1.2)

    frames = [
        "```\d      [ DOTZ UNIT - 01 ]\d\d         [🤖]\d         /|||\\\d        / ||| \\\d         |||||\d         |||||\d        /_| |_\\\d```",
        "```\d      [ DOTZ UNIT - 01 ]\d\d         [🤖]\d        /|||||\\\d       / ||||| \\\d        ||||| |\d        ||||| |\d       /_| |_\\\d```",
        "```\d      [ DOTZ UNIT - 01 ]\d\d        🔷[🤖]🔷\d        /|||||\\\d       / ||||| \\\d        ||||| |\d       ██ ██ ██\d       /_| |_\\\d```",
        "```\d      [ DOTZ UNIT - 01 ]\d\d       🔴 [🤖] 🔴\d     ░░/|||||\\░░\d    ░ / ||||| \\ ░\d     ░||||| ||░\d     ░██ ██ ██░\d     ░/_| |_|_\\░\d```",
        "```\d      [ DOTZ UNIT - 01 ]\d\d     ⚙️ SYSTEM READY ⚙️\d       🔵 [🤖] 🔵\d      /███████\\\d     / ███████ \\\d      ███ █ ███\d     ██ ██ ██ ██\d     /_|___|___\\\n```",
        "`✅ DOTZ ROBOT AKTIF. Misi dimulai...`"
    ]

    last_frame = ""
    for frame in frames:
        if frame != last_frame:
            await typew.edit(frame)
            last_frame = frame
        await asyncio.sleep(1.4)


async def spaceship(client, message):
    typew = await message.edit("🛸 Mengaktifkan mesin...")
    await asyncio.sleep(1.2)

    frames = [
        "```\n   .\n     \n     \n     \n     \n     \n```",  
        "```\n     \n     \n     \n     \n     \n   ▲\n```",
        "```\n     \n     \n     \n     \n   ▲\n  ║║\n```",
        "```\n     \n     \n     \n   ▲\n  ║║\n ╚══╝\n```",
        "```\n     \n     \n   ▲\n  ║║\n ╚══╝\n /||\\\n```",
        "```\n     \n   ▲\n  ║║\n ╚══╝\n /||\\\n/____\\\n```",
        "```\n   ▲\n  ║║\n ╚══╝\n /||\\\n/____\\\n  ||\n```",
        "```\n  🔥🔥\n   ▲\n  ║║\n ╚══╝\n /||\\\n/____\\\n  ||\n```",
        "```\n  🔥🔥\n  🔥🔥\n   ▲\n  ║║\n ╚══╝\n /||\\\n/____\\\n```",
        "`🚀 Peluncuran dalam 3...`",
        "`🚀 2...`",
        "`🚀 1...`",
        "`🚀 LIFTOFF!!!`",
        "```\n   ▲\n  ║║\n ╚══╝\n /||\\\n/____\\\n🔥🔥🔥🔥\n```",
        "```\n   ▲\n  ║║\n ╚══╝\n /||\\\n🔥🔥🔥🔥🔥🔥\n```",
        "```\n   ▲\n  ║║\n ╚══╝\n🔥🔥🔥🔥🔥🔥🔥🔥\n```",
        "`🚀 Kapal telah meninggalkan atmosfer...`",
        "`✨ Misi dimulai...`",
        "`-TAMAT-`"
    ]

    last_frame = None
    for frame in frames:
        if frame != last_frame:
            try:
                await typew.edit(frame)
                last_frame = frame
            except Exception:
                pass  
        await asyncio.sleep(1.2)


async def apocalypse(client, message):
    typew = await message.edit("`☣️ Alarm Darurat Terdengar...`")
    await asyncio.sleep(1.2)

    steps = [
        "`📢: PERINGATAN! WABAH Z TELAH MENYEBAR!`",
        "`🏃‍♂️: Kita harus pergi dari sini!`",
        "`🔦 Menyalakan senter...`",
        "`👣 Langkah kaki di lorong gelap...`",
        "`🔊 *KREEKK...* suara pintu terbuka...`",
        "`🧟‍♂️: Grrrrrrrhhhhh!!!`",
        "`💥 MENEMBAK!`",
        "`🔫 DOR! DOR! DOR!`",
        "`🧟‍♂️🧟‍♀️🧟‍♂️: Mereka datang dari segala arah!`",
        "`🚪 Mengunci pintu...`",
        "`🔋 Mengecek baterai senter... 10%`",
        "`😰 Napas mulai tak teratur...`",
        "`📻: Ada sinyal dari markas?`",
        "`📡: *Sinyal Lemah...*`",
        "`💊 Mengambil medkit...`",
        "`🔨 Siapkan senjata darurat!`",
        "`🚗 DAPAT MOBIL!`",
        "`🔑 MENYALAKAN MESIN...`",
        "`🧟‍♂️ Mengejar dari belakang!!`",
        "`🏎️ VRROOOMMMMM!!!`",
        "`💥 Menabrak kerumunan zombie!`",
        "`🌇 Akhirnya keluar dari zona merah...`",
    ]

    for step in steps:
        await typew.edit(step)
        await asyncio.sleep(1.2)

    await typew.edit("`✅ Kita selamat... untuk sekarang.`")
    await asyncio.sleep(1.2)
    await typew.edit("`🔚 - Tamat Babak Pertama -`")

async def duel(client, message):
    typew = await message.edit("`⚔️ Pertarungan Dimulai...`")
    await asyncio.sleep(1.2)

    steps = [
        "`👤: Kau tidak akan bisa mengalahkanku.`",
        "`🧙‍♂️: Kita lihat saja...`",
        "`⚡ Mengumpulkan chakra...`",
        "`🔥 Mengaktifkan mode ultimate...`",
        "`💨 DASH!!`",
        "`💥 SERANGAN PERTAMA!!!`",
        "`🛡️ Musuh Menangkis Serangan!`",
        "`🔁 Serangan Balik!!!`",
        "`💨 LOMPAT MENGHINDAR!`",
        "`🌀 Jurus Rahasia: Naga Petir!!`",
        "`⚡⚡⚡⚡⚡`",
        "`💥💥💥 BOOM!!!`",
        "`☁️ Asap menyelimuti arena...`",
        "`👁️ Musuh terjatuh!`",
        "`👤: Ternyata... kau lebih kuat...`",
        "`🧙‍♂️: Ini belum selesai...`",
        "`💫 FINAL MOVE: DIMENSI VOID!`",
        "`🌌🌌🌌🌌🌌`",
        "`💀 *Musuh Menghilang dalam Dimensi!*`",
    ]

    for step in steps:
        await typew.edit(step)
        await asyncio.sleep(1.2)

    await typew.edit("`🏁 Pertarungan Telah Usai...`")
    await asyncio.sleep(1)
    await typew.edit("`✨ Sang Pahlawan Menang! ✨`")

async def hacking(client, message):
    loading = [
        "`[■□□□□□□□□□] CONNECTING TO SERVER...`",
        "`[■■□□□□□□□□] BYPASSING FIREWALL...`",
        "`[■■■□□□□□□□] ACCESSING MATRIX CORE...`",
        "`[■■■■□□□□□□] DECODING ENCRYPTION...`",
        "`[■■■■■□□□□□] INJECTING PAYLOAD...`",
        "`[■■■■■■□□□□] UPLOADING VIRUS...`",
        "`[■■■■■■■□□□] CRACKING MAINFRAME...`",
        "`[■■■■■■■■□□] DISABLING SECURITY...`",
        "`[■■■■■■■■■□] INITIATING OVERRIDE...`",
        "`[■■■■■■■■■■] SYSTEM HACKED!`"
    ]

    glitch_effects = [
        "`#&$@! ERROR _ SYSTEM BREACH DETECTED!`",
        "`#@!*%... ::CODE OVERRIDE:: ...%@*!#`",
        "`***_DATA STREAMING_***`",
        "`> AI CORE UNLOCKED.`",
        "`> GRANTING ROOT ACCESS...`",
        "`> WELCOME, MASTER.`",
    ]

    typew = await message.edit("`Initializing hack sequence...`")
    await asyncio.sleep(1.5)

    for step in loading:
        await typew.edit(step)
        await asyncio.sleep(1)

    await asyncio.sleep(1.5)
    for glitch in glitch_effects:
        await typew.edit(glitch)
        await asyncio.sleep(1.2)

    await asyncio.sleep(1)
    await typew.edit("`> Mission Complete.`")
    await asyncio.sleep(1)
    await typew.edit("`- SYSTEM TERMINATED -`")


async def knight(client, message):
    typew = await message.edit("`Langit bergemuruh...`")
    await asyncio.sleep(1.5)
    await typew.edit("`Sang Ksatria bersiap...`")
    await asyncio.sleep(1.5)

    frames = [
        "`⚔️                  🐉`",
        "`⚔️                 🐉`",
        "`⚔️                🐉`",
        "`⚔️               🐉`",
        "`⚔️              🐉`",
        "`⚔️             🐉`",
        "`⚔️            🐉`",
        "`⚔️🔥         🐉`",
        "`⚔️🔥🔥      🐉`",
        "`⚔️🔥🔥🔥   🐉`",
        "`⚔️🔥🔥🔥🔥🐉`",
        "`⚔️💥🐉`",
        "`⚔️🐉💢`",
        "`⚔️💨     🐉`",
        "`⚔️        🐉💀`",
        "`⚔️ VICTORY! 🐉❌`"
    ]

    for frame in frames:
        await typew.edit(frame)
        await asyncio.sleep(0.6)

    await asyncio.sleep(1)
    await typew.edit("`Kerajaan aman kembali...`")
    await asyncio.sleep(1.5)
    await typew.edit("`-TAMAT-`")


async def ninja(client, message):
    typew = await message.edit("`Sunyi... tapi terasa diawasi...`")
    await asyncio.sleep(1.5)

    await typew.edit("`🌕            `")
    await asyncio.sleep(0.5)
    await typew.edit("`🌕      🥷     `")
    await asyncio.sleep(0.5)
    await typew.edit("`🌕     🥷      `")
    await asyncio.sleep(0.5)
    await typew.edit("`🌕    🥷       `")
    await asyncio.sleep(0.5)
    await typew.edit("`🌕   🥷        `")
    await asyncio.sleep(0.5)
    await typew.edit("`🌕  🥷         `")
    await asyncio.sleep(0.5)
    await typew.edit("`🌕 🥷          `")
    await asyncio.sleep(0.5)

    await typew.edit("`🥷        👤`\n`Sasaran terkunci...`")
    await asyncio.sleep(1.2)
    await typew.edit("`🥷       👤`\n`Bergerak senyap...`")
    await asyncio.sleep(1.2)
    await typew.edit("`🥷      👤`\n`Dekat... sangat dekat...`")
    await asyncio.sleep(1.2)

    await typew.edit("`🥷⚔️👤`\n`SERANGAN!!!`")
    await asyncio.sleep(1)

    await typew.edit("`🥷✅`\n`Misi selesai, tidak ada yang tahu...`")
    await asyncio.sleep(1.5)

    await typew.edit("`-TAMAT-`")


async def ufo(client, message):
    typew = await message.edit("🧍")
    frames = [
        "🧍",
        "🛸\n🧍",
        "🛸\n 🧍",
        "🛸🔦\n 🧍",
        "🛸🔦\n  🧍",
        "🛸🔦\n   🧍",
        "🛸🔦\n    🧍",
        "🛸🔦\n     🧍",
        "🛸🔦\n      😵",
        "🛸🔦\n      👤",
        "🛸🔦\n     👽",
        "`👽 Menyelesaikan penculikan...`",
        "`👽 Target berhasil diambil.`",
        "`🛸 Pergi ke galaksi lain...`",
        "`-TAMAT-`",
    ]
    
    for frame in frames:
        if typew.text != frame:
            typew = await typew.edit(frame)
        await asyncio.sleep(1)
        

async def fadmin(client, message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 20)
    await message.edit("Admin Proses....")
    animation_chars = [
            "**Promoting User As Admin...**",
            "**Enabling All Permissions To User...**",
            "**(1) Send Messages: ☑️**",
            "**(1) Send Messages: ✅**",
            "**(2) Send Media: ☑️**",
            "**(2) Send Media: ✅**",
            "**(3) Send Stickers & GIFs: ☑️**",
            "**(3) Send Stickers & GIFs: ✅**",
            "**(4) Send Polls: ☑️**",
            "**(4) Send Polls: ✅**",
            "**(5) Embed Links: ☑️**",
            "**(5) Embed Lnks: ✅**",
            "**(6) Add Users: ☑️**",
            "**(6) Add Users: ✅**",
            "**(7) Pin Messages: ☑️**",
            "**(7) Pin Messages: ✅**",
            "**(8) Change Chat Info: ☑️**",
            "**(8) Change Chat Info: ✅**",
            "**Permission Granted Successfully**",
            "**Promoted Succesfully**"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 20])


async def fleave(client, message):
    if message.forward_from:
        return

    animation_interval = 0.5
    animation_chars = [
        "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
        "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
        "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "**Chat Message Exported To** `./Inpu/`",
        "**Chat Message Exported To** `./Inpu/homework/`",
        "**Chat Message Exported To** `./Inpu/homework/groupchat.txt`",
        "__Legend is leaving this chat.....! Bye geys..__",
        "__Legend is leaving this chat.....! Bye geys..__"
    ]

    prev_text = ""
    for frame in animation_chars:
        if frame != prev_text:
            await message.edit(frame)
            prev_text = frame
        await asyncio.sleep(animation_interval)


async def tupload(client, message):
    if message.forward_from:
        return
    animation_interval = 1
    if isinstance(animation_interval, tuple):
        animation_interval = animation_interval[0]

    animation_chars = [
        "Uploading File From Telegram To Whatsapp...",
        "User Online: True\nTelegram API Access: True\nWhatsapp API Access: True\nRead Storage: True",
        "DOWNLOADING STARTED... \n\n0% [░░░░░░░░░░░░░░░░░░░░]\n`Connecting To WhatsApp API...`\nETA: 0m, 20s",
        "DOWNLOADING... \n\n11.07% [██░░░░░░░░░░░░░░░░░░]\n\nETA: 0m, 18s",
        "DOWNLOADING... \n\n20.63% [███░░░░░░░░░░░░░░░░░]\n\nETA: 0m, 16s",
        "FILE DOWNLOADED, UPLOADING TO ADMIN'S WHATSAPP GROUP [CHUTIYA GENG BOYS]... \n\n34.42% [█████░░░░░░░░░░░░░░░]\n\nETA: 0m, 14s",
        "UPLOADING... \n\n42.17% [███████░░░░░░░░░░░░░]\n\nETA: 0m, 12s",
        "UPLOADING... \n\n55.30% [█████████░░░░░░░░░░░]\n\nETA: 0m, 10s",
        "UPLOADING... \n\n64.86% [███████████░░░░░░░░░]\n\nETA: 0m, 08s",
        "UPLOADED TO ADMIN'S WHATSAPP GROUP SERVER ... \n\n74.02% [█████████████░░░░░░░]\n\nETA: 0m, 06s",
        "SPLITTING FILE IN WHATSAPP SUPPORTED SIZE & UPLOADING IT ... 86.21% [███████████████░░░░░]\n\nETA: 0m, 04s",
        "SPLITTING FILE IN WHATSAPP SUPPORTED SIZE & UPLOADING IT... 93.50% [█████████████████░░░]\n\nETA: 0m, 02s",
        "UPLOADING TO ADMIN'S WHATSAPP GROUP [MEMEX GANG BOYS]... 100% [████████████████████]\n`Scanning file...`\nETA: 0m, 00s",
        "UPLOADING FILE TO WHATSAPP GROUP COMPLETED!\nFILE VERIFIED: ✅",
        "API TERMINATED UNTIL FURTHER USAGE..."
    ]

    prev_text = ""
    for frame in animation_chars:
        if frame != prev_text:
            await message.edit(frame)
            prev_text = frame
        await asyncio.sleep(animation_interval)

async def hadiah(client, message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 17)
    await message.edit("Ada Hadiah.....")
    animation_chars = [
"⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/DOTZMUSIC)⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/DOTZMUSIC)⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/DOTZMUSIC⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/DOTZMUSIC)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/DOTZMUSIC)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/DOTZMUSIC)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://t.me/DOTZMUSIC)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://t.me/DOTZMUSIC)⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://t.me/DOTZMUSIC)⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜[🎁](https://t.me/DOTZMUSIC)⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜[🎁](https://t.me/DOTZMUSIC)⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n[🎁](https://t.me/DOTZMUSIC)⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜",
            "⬜⬜⬜\n⬜⬜⬜\n⬜⬜⬜",
            "⬜⬜\n⬜⬜",
            "[🎁](https://t.me/DOTZMUSIC)"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 17])


async def polisi(client, message):
    typew = await edit_or_reply(message, "`mek....`")
    await asyncio.sleep(1.5)
    await typew.edit("`apa tu.......!!`")
    await asyncio.sleep(1)

    dino_chase_frames = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "OUB **Polisi sedang mengejarmu sekarang**"
    ]
    
    prev_text = ""
    for frame in dino_chase_frames:
        if frame != prev_text:  
            await typew.edit(frame)
            prev_text = frame  
        await asyncio.sleep(1) 


async def solar(client, message):
    e = await edit_or_reply(message, "`solar`")
    await asyncio.sleep(1)
    
    gabut_frames = [
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
            "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
            "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
            "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
            "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
    ]

    for frame in gabut_frames:
        await e.edit(frame)
        await asyncio.sleep(0.5)


async def car(client, message):
    e = await edit_or_reply(message, "`car`")
    await asyncio.sleep(1)
    
    gabut_frames = [
"⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛🚗\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛🚗⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚗⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚗⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🚗⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛🚗⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n🚗⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬛⬜⬛\n⬛⬛⬜⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛😊⬛⬜⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "`SMILE`"
    ]

    for frame in gabut_frames:
        await e.edit(frame)
        await asyncio.sleep(0.5)


async def edit_or_reply(message, text: str):
    if message.from_user.is_self:
        return await message.edit_text(text)
    else:
        return await message.reply_text(text)


async def dot(client, message):
    typew = await edit_or_reply(message, "`Dot.....`")
    await asyncio.sleep(2)
    await typew.edit("`dot....dot....!!`")
    await asyncio.sleep(1)

    dino_chase_frames = [
        "⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**ᣃ࿈ @dotzbaikk ࿈ᣄ**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️",
        "⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**ᣃ࿈ @dotzbaikk ࿈ᣄ**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️",
        "⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**ᣃ࿈ @dotzbaikk ࿈ᣄ**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️",
        "⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**ᣃ࿈ @dotzbaikk ࿈ᣄ**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️",
        "⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**ᣃ࿈ @dotzbaikk ࿈ᣄ**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️",
        "⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**ᣃ࿈ @dotzbaikk ࿈ᣄ**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️",
        "⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**ᣃ࿈ @dotzbaikk ࿈ᣄ**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️",
        "⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**ᣃ࿈ @dotzbaikk ࿈ᣄ**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️",
        "`ᣃ࿈ @dotzbaikk ࿈ᣄ`"
    ]

    last_frame = None

    for frame in dino_chase_frames:
        if frame != last_frame:
            await typew.edit(frame)
            last_frame = frame
        await asyncio.sleep(1)


async def sinyal(client, message):
    if message.forward_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0, 24)
    await message.edit("search sinyal.....")
    animation_chars = [
"⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n🚀⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🚀⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🚀⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚀⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚀⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛🚀\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🛸⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛",
            "⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛🚶‍♂️\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n👽⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛👽⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛👽🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "__Sinyal Hilang....__"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 24])


async def bulan(client, message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(96)
    await message.edit("bulan....")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 32])


async def music(client, message):
    if message.forward_from:
        return
    animation_interval = 1.5
    animation_ttl = range(11)
    await message.edit("music....")
    animation_chars = [
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](https://t.me/DOTZMUSIC)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: @dtztelegrambot**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](https://t.me/DOTZMUSIC)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: @dtztelegrambot**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](https://t.me/DOTZMUSIC)\n\n⠀⠀⠀ **Now  Playing:Aku Titipkan Dia**\n\n**00:02** ▰▰▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: @dtztelegrambot**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](https://t.me/DOTZMUSIC)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: @dtztelegrambot**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](https://t.me/DOTZMUSIC)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: @dtztelegrambot**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](https://t.me/DOTZMUSIC)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: @dtztelegrambot**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](https://t.me/DOTZMUSIC)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: @dtztelegrambot**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](https://t.me/DOTZMUSIC)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: @dtztelegrambot**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](https://t.me/DOTZMUSIC)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: @dtztelegrambot**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](https://t.me/DOTZMUSIC)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: @dtztelegrambot**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](https://t.me/DOTZMUSIC)\n\n⠀⠀⠀⠀**Now Playing:Aku Titipkan Dia**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: @dtztelegrambot**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 11])


async def loveyou(client, message):
    noble = random.randint(1, len(NOBLE) - 2)
    reply_text = NOBLE[noble]
    await message.reply(reply_text)



async def hmm(client, message):
    return await message.reply(
        "┈┈╱▔▔▔▔▔╲┈┈┈HM┈HM\n┈╱┈┈╱▔╲╲╲▏┈┈┈HMMM\n╱┈┈╱━╱▔▔▔▔▔╲━╮┈┈\n▏┈▕┃▕╱▔╲╱▔╲▕╮┃┈┈\n▏┈▕╰━▏▊▕▕▋▕▕━╯┈┈\n╲┈┈╲╱▔╭╮▔▔┳╲╲┈┈┈\n┈╲┈┈▏╭━━━━╯▕▕┈┈┈\n┈┈╲┈╲▂▂▂▂▂▂╱╱┈┈┈\n┈┈┈┈▏┊┈┈┈┈┊┈┈┈╲\n┈┈┈┈▏┊┈┈┈┈┊▕╲┈┈╲\n┈╱▔╲▏┊┈┈┈┈┊▕╱▔╲▕\n┈▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕\n┈╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲\n┈┈╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏\n┈╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔\n┈╲▂▂▂╱┈┈┈┈╲▂▂▂╱┈ ",
    )

async def kntl(client, message):
    emoji = client.get_text(message)
    kontol = Quotly.GAMBAR_KONTOL
    if emoji:
        kontol = kontol.replace("⡀", emoji)
    await message.reply(kontol)


async def penis(client, message):
    emoji = client.get_text(message)
    titid = Quotly.GAMBAR_TITIT
    if emoji:
        titid = titid.replace("💋", emoji)
    await message.reply(titid)


async def ding(client, message):
    animation_interval = 1
    animation_ttl = range(0, 30)
    animation_chars = [
        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬛🔴\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜  [DOTZ UBOT IS THE BEST](https://t.me/dotzzuserbot) ⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
    ]
    if message.forward_from:
        return
    await message.edit("ding..dong..ding..dong ...")
    await asyncio.sleep(1.5)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 10])
        

async def hypo(client, message):
    if message.forward_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0, 15)
    await message.edit("hypo....")
    animation_chars = [
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛",
        "⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜",
        "[👉🔴👈])",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 15])
        

async def love(client, message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit("🧡💚❤️💙💛🖤💜💝💘💝")
    animation_chars = [
        "❤️🧡💛💚💙💜🖤💕💞💓",
        "🧡💚❤️💙💛🖤💜💝💘💝",
        "❤️🧡💛💚💙💜🖤💕💞💓",
        "💝💘💝💗💓💞💕🧡💚❤️",
        "❤️🧡💛💚💙💜🖤💕💞💓",
        "🧡💚❤️💙💛🖤💘💝💗💓",
        "💚❤️💙💛💞💓💗💚💙💜",
        "❤️🧡💛💚💙💜🖤💕💞💓",
        "🖤💕💞💓💘💝🧡💚❤️💙",
        "💕🧡💚❤💙💜🖤💕💞💝",
        "🧡💚❤️🖤💕💞💓💗🧡💚",
        "🧡💚❤💛🖤💕💞💓🧡💚",
        "💖💘❤️💙💛💗💓🧡🖤💜",
        "🧡💛💚💙💜🖤💕💓💗💖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 14])


async def sayang(client, message):
    e = await message.reply("I LOVEE YOUUU 💕", reply_to_message_id=Message.ReplyCheck(message))
    await e.edit("💝💘💓💗")
    await asyncio.sleep(1.5)
    await e.edit("💞💕💗💘")
    await asyncio.sleep(1.5)
    await e.edit("💝💘💓💗")
    await asyncio.sleep(1.5)
    await e.edit("💞💕💗💘")
    await asyncio.sleep(1.5)
    await e.edit("💘💞💗💕")
    await asyncio.sleep(1.5)
    await e.edit("💘💞💕💗")
    await asyncio.sleep(1.5)
    await e.edit("SAYANG KAMU 💝💖💘")
    await e.edit("💝💘💓💗")
    await asyncio.sleep(1.5)
    await e.edit("💞💕💗💘")
    await asyncio.sleep(1.5)
    await e.edit("💘💞💕💗")
    await asyncio.sleep(1.5)
    await e.edit("SAYANG")
    await asyncio.sleep(1.5)
    await e.edit("KAMU")
    await asyncio.sleep(1.5)
    await e.edit("SELAMANYA 💕")
    await asyncio.sleep(1.5)
    await asyncio.sleep(1.5)
    await e.edit("💘💘💘💘")
    await asyncio.sleep(1.5)
    await e.edit("SAYANG")
    await asyncio.sleep(1.5)
    await e.edit("KAMU")
    await asyncio.sleep(1.5)
    await e.edit("SAYANG")
    await asyncio.sleep(1.5)
    await e.edit("KAMU")
    await asyncio.sleep(1.5)
    await e.edit("I LOVE YOUUUU")
    await asyncio.sleep(1.5)
    await e.edit("MY BABY")
    await asyncio.sleep(1.5)
    await e.edit("💕💞💘💝")
    await asyncio.sleep(1.5)
    await e.edit("💘💕💞💝")
    await asyncio.sleep(1.5)
    await e.edit("SAYANG KAMU SELAMANYA💞")


async def heli(client, message):
    await message.reply(
        "▬▬▬.◙.▬▬▬ \n"
        "═▂▄▄▓▄▄▂ \n"
        "◢◤ █▀▀████▄▄▄▄◢◤ \n"
        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
        "◥█████◤ \n"
        "══╩══╩══ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ Hallo Semuanya :) \n"
        "╬═╬☻/ \n"
        "╬═╬/▌ \n"
        "╬═╬/ \\ \n",
    )


async def tembak(client, message):
    await message.reply(
        "_/﹋\\_\n"
        " (҂`_´)\n"
        "<,︻╦╤─ ҉\n"
        r"_/﹋\_"
        "\n<b>Mau Jadi Pacarku Gak?!</b>",
    )


async def bundir(client, message):
    await message.reply(
        "`Dadah Semuanya...`          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


async def otaklu(client, message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit(f"<b>This is Your Brain!</b>")
    animation_chars = [
        "Your Brain : ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "Your Brain : ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "Your Brain : ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "Your Brain : ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "Your Brain : ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "Your Brain : ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "Your Brain : ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "Your Brain : ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "Your Brain : ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "Your Brain : ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "Your Brain : ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "Your Brain : ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "Your Brain : ➡️ 🧠\n\n           (> ^_^)>🗑",
        "Your Brain : ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 14])


async def wtf(client, message):
    emo = Emoji(client)
    await emo.get()
    proses = await message.reply(f"{emo.proses} <b>Sedang proses ...</b>")
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 5)
    ro = await message.reply("wtf", reply_to_message_id=Message.ReplyCheck(message))
    animation_chars = [
        "What",
        "What The",
        "What The F",
        "What The F Brah",
        "[𝗪𝗵𝗮𝘁 𝗧𝗵𝗲 𝗙 𝗕𝗿𝗮𝗵](https://telegra.ph//file/f3b760e4a99340d331f9b.jpg)",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ro.edit(animation_chars[i % 5])
        await proses.delete()



async def gang(client, message):
    await message.edit("EVERyBOdy")
    await asyncio.sleep(1)
    await message.edit("iZ")
    await asyncio.sleep(1)
    await message.edit("GangSTur")
    await asyncio.sleep(1)
    await message.edit("UNtIL ")
    await asyncio.sleep(1)
    await message.edit("I")
    await asyncio.sleep(1)
    await message.edit("ArRivE")
    await asyncio.sleep(1)
    await message.edit("🔥🔥🔥")
    await asyncio.sleep(1)
    await message.edit("EVERyBOdy iZ GangSTur UNtIL I ArRivE 🔥🔥🔥")


async def cas(client, message):
    txt = (
        message.text[10:]
        + "\n\n`Iphone 16 Charging (Promax) Started...\nDevice Detected: Iphone 16\nBattery Percentage:` "
    )
    j = 10
    k = j
    for j in range(j):
        await message.edit(txt + str(k))
        k = k + 10
        await asyncio.sleep(1)
    await asyncio.sleep(1)
    await message.edit(
        "`Iphone 16 Charging (Promax) Completed...\nDevice Detected: Iphone 16 (gold)\nBattery Percentage:` [100%](https://telegra.ph/file/a45aa7450c8eefed599d9.mp4) ",
        disable_web_page_preview=True,
    )


async def bomb(client, message):
    if message.forward_from:
        return
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(1.2)
    await message.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(1.2)
    await message.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(1.2)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(1.2)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(1.2)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(1.2)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(1.2)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(1.2)
    await message.edit("`RIP PLOXXX......`")
    await asyncio.sleep(1.5)


async def awk(client, message):
    await message.reply(
        "────██──────▀▀▀██\n"
        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
        "▄▀──█▄▄──────█─█▄▄\n"
        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
        "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`",
    )


async def ysaja(client, message):
    await message.reply(
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n",
    )


async def tank(client, message):
    await message.reply(
        "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
        "▂▄▅█████████▅▄▃▂…\n"
        "[███████████████████]\n"
        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n",
    )


async def babi(client, message):
    await message.reply(
        "┈┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
        "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n",
    )


async def ange(client, message):
    e = await message.edit("Ayanggg 😖")
    await asyncio.sleep(2)
    await e.edit("Aku Ange 😫")
    await asyncio.sleep(2)
    await e.edit("Ayuukk Picies Yang 🤤")


async def lipkol(client, message):
    e = await message.edit("Ayanggg 😖")
    await asyncio.sleep(1)
    await e.edit("Kangeeen 👉👈")
    await asyncio.sleep(1)
    await e.edit("Pingiinn Slipkool Yaaang 🥺👉👈")


async def nakal(client, message):
    e = await message.edit("Ayanggg ih🥺")
    await asyncio.sleep(2)
    await e.edit("Nakal Banget Dah Ayang 🥺")
    await asyncio.sleep(2)
    await e.edit("Aku Gak Like Ayang 😠")
    await asyncio.sleep(2)
    await e.edit("Pokoknya Aku Gak Like Ih 😠")


async def peace(client, message):
    await message.reply(
        "┈┈┈┈PEACE MAN┈┈┈┈\n"
        "┈┈┈┈┈┈╭╮╭╮┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┃┃┃┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┃┃┃┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┗┛┣┳╮┈┈┈┈\n"
        "┈┈┈┈┈╭┻━━┓┃┃┈┈┈┈\n"
        "┈┈┈┈┈┃╲┏━╯┻┫┈┈┈┈\n"
        "┈┈┈┈┈╰╮╯┊┊╭╯┈┈┈┈\n",
    )


async def spongebob(client, message):
    await message.reply(
        "╲┏━┳━━━━━━━━┓╲╲\n"
        "╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲\n"
        "╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲\n"
        "╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲\n"
        "╲┃◯┃╭╮╰╯┏━━━┳╯╲\n"
        "╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲\n"
        "╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲\n",
    )



async def kocok(client, message):
    e = await message.edit("KOCOKINNNN SAYANGG🥵")
    await asyncio.sleep(0.5)
    await e.edit("8✊===D")
    await asyncio.sleep(0.5)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.5)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.5)
    await e.edit("8===✊D")
    await asyncio.sleep(0.5)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.5)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.5)
    await e.edit("8✊===D")
    await asyncio.sleep(0.5)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.5)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.5)
    await e.edit("8===✊D")
    await asyncio.sleep(0.5)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.5)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.5)
    await e.edit("8✊===D")
    await asyncio.sleep(0.5)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.5)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.5)
    await e.edit("8===✊D")
    await asyncio.sleep(0.5)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.5)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.5)
    await e.edit("8===✊D💦")
    await asyncio.sleep(0.5)
    await e.edit("8==✊=D💦💦")
    await asyncio.sleep(0.5)
    await e.edit("8=✊==D💦💦💦")
    await asyncio.sleep(0.5)
    await e.edit("8✊===D💦💦💦💦")
    await asyncio.sleep(0.5)
    await e.edit("8===✊D💦💦💦💦💦")
    await asyncio.sleep(0.5)
    await e.edit("8==✊=D💦💦💦💦💦💦")
    await asyncio.sleep(0.5)
    await e.edit("8=✊==D💦💦💦💦💦💦💦")
    await asyncio.sleep(0.5)
    await e.edit("8✊===D💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.5)
    await e.edit("8===✊D💦💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.5)
    await e.edit("8==✊=D💦💦💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.5)
    await e.edit("**CROOTTTT**")
    await asyncio.sleep(0.5)
    await e.edit("**CROOTTTT AAAHHH.....**")
    await asyncio.sleep(0.5)
    await e.edit("AHHH ENAKKKKK SAYANGGGG🥵🥵**")


async def gabut(client, message):
    teks = [
        "PERNAAHHHHH KAH KAUUU MENGIRA",
        "SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA",
        "RAMBUUUT WARNAAA WARNII", "BAGAI GULALI", "IMUUUTTTTT LUCUUU",
        "WALAAUUUU TAK TERLALU TINGGI", "GW GABUUTTTT", "EMMMM BACOTNYA",
        "GABUTTTT WOI GABUT", "🙈🙈🙈🙈", "🙉🙉🙉🙉", "🙈🙈🙈🙈", "🙉🙉🙉🙉", "CILUUUKKK BAAAAA",
        "🙉🙉🙉🙉", "🐢🚶", "`AHHH MANTAP`", "🙉", "🙈", "🙉", "🙈", "🙉", "😂", "`GABUT BANGET COK`"
    ]

    anim1 = [f"🐢{' ' * i}🚶" for i in reversed(range(25))]
    anim2 = [f"🚶{' ' * i}🐢" for i in range(25)]

    e = await message.reply(teks[0], reply_to_message_id=Message.ReplyCheck(message))

    for t in teks[1:7]:
        await asyncio.sleep(1)
        await e.edit(f"`{t}`")

    for t in teks[7:14]:
        await asyncio.sleep(0.5)
        await e.edit(t)

    for frame in anim1:
        await asyncio.sleep(0.5)
        await e.edit(frame)

    await asyncio.sleep(1)
    for frame in anim2:
        await asyncio.sleep(0.5)
        await e.edit(frame)

    for t in teks[14:]:
        await asyncio.sleep(1)
        await e.edit(t)


async def dino(client, message):
    typew = await message.edit("`DIN DINNN.....`")
    await asyncio.sleep(1.5)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    await asyncio.sleep(1.5)

    for i in range(24, 16, -1):
        await typew.edit(f"`🏃{' ' * i}🦖`")
        await asyncio.sleep(0.15)

    await typew.edit("`🏃   `LARII`          🦖`")
    await asyncio.sleep(0.5)

    for i in range(15, 11, -1):
        await typew.edit(f"`🏃{' ' * i}🦖`")
        await asyncio.sleep(0.15)

    await typew.edit("`🏃     Roarrwww            🦖`")
    await asyncio.sleep(0.5)

    for i in range(10, 2, -1):
        await typew.edit(f"`🏃{' ' * i}🦖`")
        await asyncio.sleep(0.12)

    await typew.edit("`🏃WOARGH!   🦖`")
    await asyncio.sleep(0.5)

    for i in range(3, 10):
        await typew.edit(f"`🏃{' ' * i}🦖`")
        await asyncio.sleep(0.12)

    await typew.edit("`🏃  Huh-Huh           🦖`")
    await asyncio.sleep(0.5)

    for i in range(11, 4, -1):
        await typew.edit(f"`🏃{' ' * i}🦖`")
        await asyncio.sleep(0.5)

    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    await asyncio.sleep(1)

    for i in range(7, 3, -1):
        await typew.edit(f"`🏃{' ' * i}🦖`")
        await asyncio.sleep(0.5)

    await typew.edit("`Dahlah Pasrah Aja Cok`")
    await asyncio.sleep(1.5)

    await typew.edit("`🧎🦖`")
    await asyncio.sleep(1)

    await typew.edit("`-TAMAT-`")



async def anjg(client, message):
    await message.reply(
        "╥━━━━━━━━╭━━╮━━┳\n"
        "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
        "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
        "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
        "╨━━┗┛┗┛━━┗┛┗┛━━┻\n",
    )


async def nahlove(client, message):
    typew = await message.reply("`\n(\\_/)`" "`\n(●_●)`" "`\n />💖 *Ini Buat Kamu`")
    await asyncio.sleep(1.5)
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n💖<\\  *Tapi Bo'ong`")


async def tq(client, message):
    await message.reply(
        "╔══╦╗────╔╗─╔╗╔╗\n"
        "╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗\n"
        "─║║║║║╬║║║╩║╚╗╔╣║║║║\n"
        "─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\n"
    )


async def rumah(client, message):
    await message.reply(
        "╱◥◣\n"
        "│∩ │◥███◣ ╱◥███◣\n"
        "╱◥◣ ◥████◣▓∩▓│∩ ║\n"
        "│╱◥█◣║∩∩∩ ║◥█▓ ▓█◣\n"
        "││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║\n"
        "๑۩๑๑۩๑๑ ۩๑๑۩๑▓๑۩๑๑۩๑"
    )



async def syg(client, message):
    await message.edit("sayang..")
    await asyncio.sleep(1.5)
    await message.edit("❤️ I")
    await asyncio.sleep(1)
    await message.edit("❤️ I Love")
    await asyncio.sleep(1)
    await message.edit("❤️ I Love You")
    await asyncio.sleep(1.5)
    await message.edit("❤️ I Love You <3")


async def hack(client, message):
    await message.edit("hack akun aktif...")
    await asyncio.sleep(2)
    await message.edit(" User online: True\nTelegram access: True\nRead Storage: True ")
    await asyncio.sleep(2)
    await message.edit(
        "Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for Telegram...`\nETA: 0m, 20s"
    )
    await asyncio.sleep(2)
    await message.edit(
        "Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for Telegram...`\nETA: 0m, 18s"
    )
    await asyncio.sleep(2)
    await message.edit(
        "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder C:/Telegram`\nETA: 0m, 16s"
    )
    await asyncio.sleep(2)
    await message.edit(
        "Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder C:/Telegram`\nETA: 0m, 14s"
    )
    await asyncio.sleep(2)
    await message.edit(
        "Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s"
    )
    await asyncio.sleep(2)
    await message.edit(
        "Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s"
    )
    await asyncio.sleep(2)
    await message.edit(
        "Hacking... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s"
    )
    await asyncio.sleep(2)
    await message.edit(
        "Hacking... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s"
    )
    await asyncio.sleep(2)
    await message.edit(
        "Hacking... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s"
    )
    await asyncio.sleep(2)
    await message.edit(
        "Hacking... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s"
    )
    await asyncio.sleep(2)
    await message.edit(
        "Hacking... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s"
    )
    await asyncio.sleep(2)
    await message.edit("Hacking complete!\nUploading file...")
    await asyncio.sleep(2)
    await message.edit(
        "Targeted Account Hacked...!\n\n ✅ File has been successfully uploaded to my server.\nTelegram Database:\n`./DOWNLOADS/msgstore.db.crypt12`"
    )


async def santet(client, message):
    typew = await message.reply("`Mengaktifkan Perintah Santet Online....`")
    await asyncio.sleep(1.5)
    await typew.edit("`Mencari Nama Orang Ini...`")
    await asyncio.sleep(1.5)
    await typew.edit("`Santet Online Segera Dilakukan`")
    await asyncio.sleep(1.5)
    await typew.edit("0%")
    number = 1
    await typew.edit(str(number) + "%   ▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████▊")
    number += 1
    await asyncio.sleep(1.5)
    await typew.edit(str(number) + "%   ████████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████████▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████████▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   █████████████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████████▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ██████████████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████████▊")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ███████████████▉")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████████████")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████████████▎")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████████████▍")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████████████▌")
    number += 1
    await asyncio.sleep(1)
    await typew.edit(str(number) + "%   ████████████████▌")
    await asyncio.sleep(1)
    await typew.edit("<b>Target Berhasil Tersantet Online Brok 🥴</b>")







