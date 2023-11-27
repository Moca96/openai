from os import environ
from pyrogram import Client, filters, enums
import openai

API = environ.get("API","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")
API_ID = environ.get("API_ID","28074580")
API_HASH = environ.get("API_HASH","902a80b6c54c4cbd58e240ee241cfcbf")
BOT_TOKEN = environ.get("BOT_TOKEN","6877447745:AAEOKZ8MstrvCaElzwTJ3LFHVT04cQ9qzCI")

app = Client(
    "chatgpt",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.private & filters.command("start"))
async def start(app, message):
    await message.reply(
        f"**Hey {message.from_user.mention} \n\nIam An Advance ChatGpt Bot To Assist Yout. How Can I Help You?**")

@app.on_message(filters.private & filters.text)
async def chatgpt(app, message):
    openai.api_key = API
    try:
        msg = message.text
        user_id = message.from_user.id
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = msg,
            temperature = 0.5, 
            max_tokens = 1000,
            top_p=1,
            frequency_penalty=0.1,
            presence_penalty = 0.0,
        )
        response = response.choices[0].text 
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message.reply(f"{response}")
    except Exception as error:
        print(error)


    
app.run()
