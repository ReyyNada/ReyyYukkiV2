#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import random

from pyrogram.types import InlineKeyboardButton

selections = [
    "▁▄▂▇▄▅▄▅▃",
    "▁▃▇▂▅▇▄▅▃",
    "▃▁▇▂▅▃▄▃▅",
    "▃▄▂▄▇▅▃▅▁",
    "▁▃▄▂▇▃▄▅▃",
    "▃▁▄▂▅▃▇▃▅",
    "▁▇▄▂▅▄▅▃▄",
    "▁▃▅▇▂▅▄▃▇",
    "▃▅▂▅▇▁▄▃▁",
    "▇▅▂▅▃▄▃▁▃",
    "▃▇▂▅▁▅▄▃▁",
    "▅▄▇▂▅▂▄▇▁",
    "▃▅▂▅▃▇▄▅▃",
]


## After Edits with Timer Bar


def stream_markup_timer(_, videoid, chat_id, played, dur):
    bar = random.choice(selections)
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text=_["PL_B_3"],
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    bar = random.choice(selections)
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_3"],
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


## Inline without Timer Bar


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text=_["PL_B_3"],
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_3"],
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
