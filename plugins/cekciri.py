__MODULES__ = "Cekciri"
__HELP__ = """<blockquote>Command Help <b>Cekciri</b></blockquote>

<blockquote expandable>--**Fun Personality Checks**--

    ❖ **Check jodoh level of your couple**
        `{0}cekjdh` (reply or username)    
    ❖ **Check kontol level of a person**
        `{0}cekkntl` (reply or username)
    ❖ **Check memek level of a person**
        `{0}cekmmk` (reply or username)
    ❖ **Check sange status of a person**
        `{0}ceksange` (reply or username)
    ❖ **Check religion of a person**
        `{0}cekagama` (reply or username)</blockquote>
<b>   {1}</b>
"""

IS_PRO = True

from command import cekjdh_cmd, cekkntl_cmd, cekmmk_cmd, ceksange_cmd, cekagama_cmd
from helpers import CMD


@CMD.UBOT("cekjdh")
async def _(client, message):
    return await cekjdh_cmd(client, message)
    

@CMD.UBOT("cekkntl")
async def _(client, message):
    return await cekkntl_cmd(client, message)

@CMD.UBOT("cekmmk")
async def _(client, message):
    return await cekmmk_cmd(client, message)

@CMD.UBOT("ceksange")
async def _(client, message):
    return await ceksange_cmd(client, message)

@CMD.UBOT("cekagama")
async def _(client, message):
    return await cekagama_cmd(client, message)