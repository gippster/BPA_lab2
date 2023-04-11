import logging
from aiogram import Bot, Dispatcher, executor, types
def Botfunc(mean):
    bot = Bot(token="6277453202:AAGydD69wQ-ZkJnWTce5MU45cGd_bxm8E0Y")
    # Диспетчер для бота
    dp = Dispatcher(bot)
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)


    @dp.message_handler(text="course")
    async def cmd_test1(message: types.Message):
        if mean > 80.0:
            await message.reply("Курс вырос свыше 80: " + str(mean) + " Российских рублей")
        elif mean < 75.0:
            await message.reply("Курс упал ниже 75: " + str(mean) + " Российских рублей")
        else:
            await message.reply("Курс в пределах от 75 до 80: " + str(mean) + " Российских рублей")
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
