from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from datetime import datetime
import pytz
import jdatetime

# توکن رباتت رو اینجا بذار
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['time'])
async def send_time(message: types.Message):
    # زمان ایران
    tehran_tz = pytz.timezone("Asia/Tehran")
    tehran_time = datetime.now(tehran_tz)
    jdate = jdatetime.datetime.fromgregorian(datetime=tehran_time)

    # زمان UTC
    utc_time = datetime.utcnow()

    # ترجمه روز و ماه فارسی
    weekdays_fa = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه", "یک‌شنبه"]
    months_fa = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

    weekday_fa = weekdays_fa[jdate.weekday()]
    weekday_en = tehran_time.strftime("%A")
    month_fa = months_fa[jdate.month - 1]
    month_en = tehran_time.strftime("%B")

    # ساخت متن خروجی
    text = (
        f"Tehran Time : ( {tehran_time.strftime('%H:%M:%S')} )\n\n"
        f"Date :\n"
        f"   Full : ( {jdate.strftime('%Y/%m/%d')} - {tehran_time.strftime('%Y/%m/%d')} )\n"
        f"   Day : ( {weekday_fa} - {weekday_en} )\n"
        f"   Month : ( {month_fa} - {month_en} )\n\n"
        f"UTC :\n"
        f"   ( {utc_time.strftime('%A %Y-%m-%d %H:%M:%S')} )"
    )

    await message.reply(text)

if __name__ == '__main__':
    executor.start_polling(dp)
