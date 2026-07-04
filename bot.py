import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Logging
logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Welcome to CryptoGuard Bot!\n\n"
        "Real-time price alerts + AI Analysis\n\n"
        "Commands:\n"
        "/price <symbol> - Current price\n"
        "/alert <symbol> <price> - Set alert\n"
        "/analyze <symbol> - AI Analysis\n"
        "/pro - Upgrade to Pro"
    )

@dp.message(Command("price"))
async def price(message: types.Message):
    # فعلاً ساده
    await message.answer("🔄 Price checking feature coming soon...")

@dp.message(Command("pro"))
async def pro(message: types.Message):
    await message.answer(
        "🚀 Pro Version:\n\n"
        "Price: 20 USDT / month\n"
        "Send USDT to this address or use /pay"
    )

# Echo for testing
@dp.message()
async def echo(message: types.Message):
    await message.answer("Echo: " + message.text)

async def main():
    print("🚀 CryptoGuard Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
