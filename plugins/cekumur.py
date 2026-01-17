__MODULES__ = "Cekumur"
__HELP__ = """<blockquote>Command Help **cek umur**</blockquote>
<blockquote expandable>--**Basic Commands**--

    ❖ **Check Fakta umur**
        `{0}cekumur` (query)</blockquote>
<b>   {1}</b>
"""


from command import cekumur_cmd
from helpers import CMD

IS_PRO = True


@CMD.UBOT("cekumur")
async def _(client, message):
    return await cekumur_cmd(client, message)
