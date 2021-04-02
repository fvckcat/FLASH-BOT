# pikiiii ganteng

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register

# piki


@register(outgoing=True, pattern=r"^.tempmail ?(.*)")
async def demn(event):
    chat = "@TempMailBot"
    await event.edit("Sedang Memprosess...")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.await_event(events.NewMessage(
                incoming=True,
                from_users=220112646
            )
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("Generate New")
            response = await response
            ((response).reply_markup.rows[2].buttons[0].url)
            await bot.send_read_acknowledge(chat)
        except YouBlockedUserError:
            await event.edit("Mohon Unblock @TempMailBot !!!")
            return
        await event.edit("TEMPMAIL ~ `{response.message.message}`\n\n[KLIK DISINI UNTUK MELIHAT VERIFIKASI]({link})")


# Piki Gantengg
CMD_HELP.update(
    {
        "tempmail": "**Modules:** __Temp Mail__\n\n**Perintah:** `.tempmail`"
        "\n**Penjelasan:** Mendapatkan Email Gratis Dari Temp Mail"})
