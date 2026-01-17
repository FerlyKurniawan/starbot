__MODULES__ = "Cektt"
__HELP__ = """<blockquote>Command Help **cek tt**</blockquote>
<blockquote expandable>--**Basic Commands**--

    ❖ **Check Fakta tt**
        `{0}cektt` (query)</blockquote>
<b>   {1}</b>
"""


from command import cektt_cmd
from helpers import CMD

IS_PRO = True


@CMD.UBOT("cektt")
async def _(client, message):
    return await cektt_cmd(client, message)
