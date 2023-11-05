import asyncio
import logging
import sys
import g4f

from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand, BotCommandScopeDefault
from aiogram.utils.markdown import hbold
from controller import run_web_service

load_dotenv()
TOKEN = getenv("TELEGRAM_BOT_API_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command("info"))
async def command_start_handler(message: Message) -> None:
    msg_info = ("Этот дружелюбный бот готов поддержать разговор и ответить на вопросы. "
                "Для генерации ответов используются модели GPT.")
    await message.answer(msg_info)


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": message.text}]
        )
        if response == "":
            answer = "No response received. Please try again"
        else:
            answer = response

        await message.answer(answer)
    except TypeError:
        await message.answer("Nice try!")


def get_commands():
    return [
        BotCommand(command="info", description="Справка")
    ]


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.set_my_commands(get_commands(), BotCommandScopeDefault())
    await dp.start_polling(bot)


run_web_service()
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
