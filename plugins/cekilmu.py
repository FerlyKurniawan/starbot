__MODULES__ = "Cekilmu"
__HELP__ = """<blockquote>Command Help **cek ilmu**</blockquote>
<blockquote expandable>--**Basic Commands**--

    ❖ **Check Fakta ilmu**
        `{0}cekilmu` (query)</blockquote>
<b>   {1}</b>
"""


from command import cekilmu_cmd
from helpers import CMD

IS_PRO = True


@CMD.UBOT("cekilmu")
async def _(client, message):
    return await cekilmu_cmd(client, message)
