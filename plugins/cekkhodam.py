__MODULES__ = "Cekkhodam"
__HELP__ = """<blockquote>Command Help **cek khodam**</blockquote>
<blockquote expandable>--**Basic Commands**--

    ❖ **Check Fakta khodam**
        `{0}cekhodam` (query)</blockquote>
<b>   {1}</b>
"""


from command import cekkhodam_cmd
from helpers import CMD

IS_PRO = True


@CMD.UBOT("cekkhodam")
async def _(client, message):
    return await cekkhodam_cmd(client, message)
