__MODULES__ = "Cekjembut"
__HELP__ = """<blockquote>Command Help **cek jembut**</blockquote>
<blockquote expandable>--**Basic Commands**--

    ❖ **Check Fakta jembut**
        `{0}ceklahir` (query)</blockquote>
<b>   {1}</b>
"""


from command import cekjembut_cmd
from helpers import CMD

IS_PRO = True


@CMD.UBOT("cekjembut")
async def _(client, message):
    return await cekjembut_cmd(client, message)
