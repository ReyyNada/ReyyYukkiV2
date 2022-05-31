#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.


import asyncio

from pyrogram import Client as c

API_ID = input("\nKirim API_ID Anda:\n > ")
API_HASH = input("\nKirim API_HASH Anda:\n > ")

print("\n\n Masukkan nomor telepon saat ditanya.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nINI ADALAH SESI STRING ANDA, SALIN, JANGAN BAGIKAN!!\n")
    print(f"\n{ss}\n")


asyncio.run(main())
