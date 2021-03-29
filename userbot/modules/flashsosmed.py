# Port by Koala 🐨/@manuskarakitann
# Untuk FLASH-BOT

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP

# Toni Baik Makasih Sama-Sama


@register(outgoing=True, pattern="^.dpint ?(.*)")
@register(outgoing=True, pattern="^.dtik ?(.*)")
@register(outgoing=True, pattern="^.dig ?(.*)")
async def insta(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Balas Ke link Untuk Mengunduh Media.`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Balas Ke Link Untuk Mengunduh.`")
        return
    chat = "@SaveAsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Sedang Memprosess...")
        return
    await event.edit("`Mohon Tunggu...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("@SaveAsbot'u `Mohon Unblock Dulu Botnya`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Tolong Jangan Di Private"
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"Woowwww⚡",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
            await event.delete()


@register(outgoing=True, pattern="^.dez(?: |$)(.*)")
async def DeezLoader(event):
    if event.fwd_from:
        return
    dlink = event.pattern_match.group(1)
    if ".com" not in dlink:
        await event.edit("`Tolong Balas Ke Link Untuk Mengunduh Media`")
    else:
        await event.edit("**Sedang Di Prosess, Mohon Tunggu** 🎶")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.get_response()
            await conv.send_message(dlink)
            details = await conv.get_response()
            song = await conv.get_response()
#                                   #
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("@DeezLoadBot'Mohon Di Unblock")
            return
        await bot.send_file(event.chat_id, song, caption=details.text)

CMD_HELP.update(
    {
        "sosmed": ">`.dpint`"
        "\nUsage: Untuk Mengunduh Media Dari Pinterest"
        "\n\n>`.dtik`"
        "\nUsage: Untuk Mengunduh Media/Video Dari Tiktok"
        "\n\n>`.dig`"
        "\nUsage: Untuk Mengunduh Media/Video Dari Instagram"
        "\n\n>`.dez`"
        "\nUsage: Untuk Mengunduh Music"


    }
)
