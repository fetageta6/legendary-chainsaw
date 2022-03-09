import os
from pyrogram import filters
from bot import LOG, app, advance_config, chats_data, from_chats

LOG.info("Welcome, this is the telegram-message-forwarder-bot. main routine...")

@app.on_message(filters.chat(from_chats) & filters.incoming & filters.photo)
def work(client, message):
    caption = None
    msg = None
    if advance_config:
        try:
            for chat in chats_data[message.chat.id]:
                if caption:
                    message.copy(chat, caption=caption)
                else:
                    message.copy(chat)
        except Exception as e:
            LOG.error(e)

app.run()
