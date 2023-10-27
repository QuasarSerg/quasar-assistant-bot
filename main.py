from dotenv import load_dotenv
import os
import telebot
import g4f
from fastapi import FastAPI

app = FastAPI()
load_dotenv()

bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_API_TOKEN'), threaded=False)

bot.set_my_commands([
    telebot.types.BotCommand("/info", 'Справка')
])


@app.get("/")
async def root():
    return {"message": "👋"}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/info':
        bot.send_message(message.from_user.id, '👋')
    else:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=[{"role": "user", "content": message.text}],
        )
        bot.send_message(message.from_user.id, response)


if __name__ == '__main__':
    bot.infinity_polling()
