__MODULES__ = "Ceklahir"
__HELP__ = """<blockquote>Command Help **cek lahir**</blockquote>
<blockquote expandable>--**Basic Commands**--

    ❖ **Check Fakta Lahir**
        `{0}ceklahir` (query)</blockquote>
<b>   {1}</b>
"""


from command import ceklahir_cmd
from helpers import CMD

IS_PRO = True


@CMD.UBOT("ceklahir")
async def _(client, message):
    return await ceklahir_cmd(client, message)
