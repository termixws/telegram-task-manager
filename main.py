import os
import asyncio
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReactionTypeEmoji


load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message : Message):
    await message.reply(f"Hello. \nYour ID: {message.from_user.id}. \nName: {message.from_user.first_name}.")

@dp.message(Command('help'))
async def ge_help(message : Message):
    await message.answer("command /help")

@dp.message(F.text =='sup')
async def hello(message : Message):
    await message.answer("what's up homie")

@dp.message(F.photo)
async def get_photo(message : Message):
    await message.answer(f"ID Photo: {message.photo[-1].file_id}")

@dp.message(Command('qwe'))
async def get_qwe(message : Message):
    await message.react(reaction=[ReactionTypeEmoji(emoji="❤")])
    

@dp.message(Command('get_photo'))
async def send_photo(message : Message):
    await message.answer_photo(photo='AgACAgEAAxkBAANVabvSyM8Pp3jiJ-62RYPNAjR19EUAAocLaxvGrOFF3AklOpHFfE8BAAMCAAN4AAM6BA',
                               caption='Just photo')

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")