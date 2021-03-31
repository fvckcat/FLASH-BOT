# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Maaf Bee, Saya Tidak Punya Perintah Itu.**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        await event.edit("⚡")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t⚡  "
        await event.edit("𝘿𝙖𝙛𝙩𝙖𝙧 𝙥𝙚𝙧𝙞𝙣𝙩𝙖𝙝 𝙪𝙣𝙩𝙪𝙠\n⚡𝙁𝙇𝘼𝙎𝙃-𝘽𝙊𝙏:\n\n"
                         f"⚡{string}⚡"
                         "\n━━━━━━━━━━━━━━━━━━━━━━━━")
        await event.reply(f"\n__Ketik Contoh__ __.help afk__ __Untuk Informasi Perintah__")
        await asyncio.sleep(1000)
        await event.delete()
