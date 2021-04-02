from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.tempmail(?: |$)(.*)")
async def _(event):
    chat = "@TempMailBot"
    msg = await event.edit("Generating Temporary Mail...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=220112646
            )
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("Generate New")
            response = await response
            link = ((response).reply_markup.rows[2].buttons[0].url)
            await ultroid_bot.send_read_acknowledge(chat)
        except YouBlockedUserError:
            await msg.edit("Boss! Please Unblock @TempMailBot ")
            return
        await eor(ult, f"TEMPMAIL ~ `{response.message.message}`\n\n[CLICK TO VIEW INBOX]({link})")



HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
