import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import pytz
import jdatetime
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("time"))
async def send_time(message: types.Message):
    tz = pytz.timezone("Asia/Tehran")
    tehran_now = datetime.now(tz)
    utc_now = datetime.utcnow()
    jalali_now = jdatetime.datetime.fromgregorian(datetime=tehran_now)

    reply = f"""Tehran Time : ( {tehran_now.strftime('%H:%M:%S')} )

Date :
   Full : ( {jalali_now.strftime('%Y/%m/%d')} - {tehran_now.strftime('%Y-%m-%d')} )
   Day : ( {jalali_now.strftime('%A')} - {tehran_now.strftime('%A')} )
   Month : ( {jalali_now.strftime('%B')} - {tehran_now.strftime('%B')} )

UTC :
   ( {utc_now.strftime('%A %Y-%m-%d %H:%M:%S')} )
"""
    await message.answer(reply)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
