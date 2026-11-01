import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# توکن ربات خودت را اینجا به جای عبارت داخل کوتیشن قرار بده
TOKEN = "9124513692:AAGTIFqpOD4_tInmwTI7fMabmrK4zuChrSA"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"سلام {html.bold(message.from_user.full_name)}! خوش آمدی به فروشگاه استارز ما 🌟\nبه زودی قابلیت خرید استارز اینجا فعال می‌شود.")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
