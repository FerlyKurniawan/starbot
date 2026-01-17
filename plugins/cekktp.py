__MODULES__ = "Cekktp"
__HELP__ = """<blockquote>Command Help **cek ktp**</blockquote>
<blockquote expandable>--**Basic Commands**--

    ❖ **Check Fakta ktp**
        `{0}cekktp` (query)</blockquote>
<b>   {1}</b>
"""


from command import cekktp_cmd
from helpers import CMD

IS_PRO = True


@CMD.UBOT("cekktp")
async def _(client, message):
    return await cekktp_cmd(client, message)
