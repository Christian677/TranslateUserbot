from pyrogram import Client, filters

from python_translator import Translator


api_id = 
api_hash = 


app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.me)
async def my_handler(client, message):

    translator = Translator()
    result = translator.translate(message.text, "english", "italian")

    await client.edit_message_text(
    chat_id=message.chat.id,
    message_id=message.id,
    text=result

)


app.run()