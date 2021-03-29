""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.flashhelp$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Kurang Paham Dengan Fitur Flash-Bot, Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/bluuebluesky)"
        "\n[Repo](https://github.com/fvckcat/FLASH-BOT)"
        "\n[Instagram](Instagram.com/antoniprananda)")


@register(outgoing=True, pattern="^.flashvar$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/fvckcat/FLASH-BOT/FLASH-BOT/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.flashhelp`\
\nUsage: Bantuan Untuk Flash-Bot.\
\n`.flashvar`\
\nUsage: Melihat Daftar Vars Flash-Bot."
})
