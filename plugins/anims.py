from command import (fadmin, fleave, tupload, hadiah, polisi, solar, car, dot, 
                     sinyal, bulan, music, loveyou, kntl, penis, ding, hypo, 
                     love, sayang, heli, tembak, bundir, otaklu, wtf, gang, cas, 
                     bomb, awk, ysaja, tank, babi, ange, lipkol, nakal, peace, 
                     spongebob, kocok, gabut, dino, anjg, nahlove,  tq, rumah, 
                     syg, hack, santet, hmm, ufo, ninja, knight, hacking, duel, 
                     apocalypse, spaceship, robot, dotz)
from helpers import CMD

DEFAULTUSER = "Nay"


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


__MODULES__ = "Animasi"
__HELP__ = """<blockquote>Command Help **Animasi**</blockquote>
<blockquote expandable>--**All command**-- 

    **You can use this command for animasi**
 ✧ `{0}dino`    | `{0}nakal`     | `{0}bomb`
 ✧ `{0}ange`    | `{0}kocok`     | `{0}cas`
 ✧ `{0}hack`    | `{0}syg`       | `{0}gangbang`
 ✧ `{0}kntl`    | `{0}ajg`       | `{0}wtf`
 ✧ `{0}heli`    | `{0}nah`       | `{0}love`
 ✧ `{0}peace`   | `{0}hmm`       | `{0}sayang`
 ✧ `{0}tank`    | `{0}awk`       | `{0}gabut`
 ✧ `{0}loveyou` | `{0}lipkol`    | `{0}hypo`
 ✧ `{0}rumah`   | `{0}tembak`    | `{0}ding`
 ✧ `{0}bundir`  | `{0}spongebob` | `{0}music`
 ✧ `{0}y`       | `{0}tq`        | `{0}bulan`
 ✧ `{0}santet`  | `{0}otaklu`    | `{0}sinyal`
 ✧ `{0}dot`     | `{0}car`       | `{0}fadmin`
 ✧ `{0}fleave`  | `{0}tupload`   | `{0}hadiah`
 ✧ `{0}solar`   | `{0}apocal`    | `{0}duel`
 ✧ `{0}ninja`   | `{0}knight`    | `{0}hacking`
 ✧ `{0}ufo`     | `{0}dotz`      | `{0}robot` 
 ✧ `{0}spaceship`</blockquote>
<b>   {1}</b>
"""

@CMD.UBOT("spaceship")
async def _(client, message):
    return await spaceship(client, message)

@CMD.UBOT("robot")
async def _(client, message):
    return await robot(client, message)

@CMD.UBOT("dotz")
async def _(client, message):
    return await dotz(client, message)

@CMD.UBOT("apocal")
async def _(client, message):
    return await apocalypse(client, message)

@CMD.UBOT("duel")
async def _(client, message):
    return await duel(client, message)

@CMD.UBOT("hacking")
async def _(client, message):
    return await hacking(client, message)

@CMD.UBOT("knight")
async def _(client, message):
    return await knight(client, message)

@CMD.UBOT("ninja")
async def _(client, message):
    return await ninja(client, message)

@CMD.UBOT("ufo")
async def _(client, message):
    return await ufo(client, message)


@CMD.UBOT("hmm")
async def _(client, message):
    return await hmm(client, message)
  

@CMD.UBOT("fadmin")
async def _(client, message):
    return await fadmin(client, message)


@CMD.UBOT("fleave")
async def _(client, message):
    return await fleave(client, message)


@CMD.UBOT("kntl")
async def _(client, message):
    return await kntl(client, message)


@CMD.UBOT("tupload")
async def _(client, message):
    return await tupload(client, message)


@CMD.UBOT("hadiah")
async def _(client, message):
    return await hadiah(client, message)


@CMD.UBOT("polisi")
async def _(client, message):
    return await polisi(client, message)


@CMD.UBOT("solar")
async def _(client, message):
    return await solar(client, message)


@CMD.UBOT("car")
async def _(client, message):
    return await car(client, message)


@CMD.UBOT("dot")
async def _(client, message):
    return await dot(client, message)


@CMD.UBOT("sinyal")
async def _(client, message):
    return await sinyal(client, message)


@CMD.UBOT("bulan")
async def _(client, message):
    return await bulan(client, message)


@CMD.UBOT("music")
async def _(client, message):
    return await music(client, message)


@CMD.UBOT("loveyou")
async def _(client, message):
    return await loveyou(client, message)


@CMD.UBOT("kntl")
async def _(client, message):
    return await kntl(client, message)


@CMD.UBOT("penis")
async def _(client, message):
    return await penis(client, message)


@CMD.UBOT("ding")
async def _(client, message):
    return await ding(client, message)


@CMD.UBOT("hypo")
async def _(client, message):
    return await hypo(client, message)


@CMD.UBOT("love")
async def _(client, message):
    return await love(client, message)


@CMD.UBOT("sayang")
async def _(client, message):
    return await sayang(client, message)


@CMD.UBOT("heli")
async def _(client, message):
    return await heli(client, message)


@CMD.UBOT("tembak")
async def _(client, message):
    return await tembak(client, message)


@CMD.UBOT("bundir")
async def _(client, message):
    return await bundir(client, message)


@CMD.UBOT("otaklu")
async def _(client, message):
    return await otaklu(client, message)


@CMD.UBOT("wtf")
async def _(client, message):
    return await wtf(client, message)

@CMD.UBOT("gangbang")
async def _(client, message):
    return await gang(client, message)


@CMD.UBOT("cas")
async def _(client, message):
    return await cas(client, message)


@CMD.UBOT("bomb")
async def _(client, message):
    return await bomb(client, message)


@CMD.UBOT("awk")
async def _(client, message):
    return await awk(client, message)


@CMD.UBOT("y")
async def _(client, message):
    return await ysaja(client, message)


@CMD.UBOT("tank")
async def _(client, message):
    return await tank(client, message)


@CMD.UBOT("babi")
async def _(client, message):
    return await babi(client, message)


@CMD.UBOT("ange")
async def _(client, message):
    return await ange(client, message)


@CMD.UBOT("lipkol")
async def _(client, message):
    return await lipkol(client, message)


@CMD.UBOT("nakal")
async def _(client, message):
    return await nakal(client, message)


@CMD.UBOT("peace")
async def _(client, message):
    return await peace(client, message)


@CMD.UBOT("spongebob")
async def _(client, message):
    return await spongebob(client, message)


@CMD.UBOT("kocok")
async def _(client, message):
    return await kocok(client, message)


@CMD.UBOT("gabut")
async def _(client, message):
    return await gabut(client, message)


@CMD.UBOT("dino")
async def _(client, message):
    return await dino(client, message)

@CMD.UBOT("ajg")
async def _(client, message):
    return await anjg(client, message)


@CMD.UBOT("nah")
async def _(client, message):
    return await nahlove(client, message)


@CMD.UBOT("tq")
async def _(client, message):
    return await tq(client, message)


@CMD.UBOT("rumah")
async def _(client, message):
    return await rumah(client, message)


@CMD.UBOT("syg")
async def _(client, message):
    return await syg(client, message)


@CMD.UBOT("hack")
async def _(client, message):
    return await hack(client, message)


@CMD.UBOT("santet")
async def _(client, message):

    return await santet(client, message)


