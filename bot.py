import logging
from aiogram import Bot, Dispatcher, executor, types
def Botfunc():
    bot = Bot(token="6277453202:AAGydD69wQ-ZkJnWTce5MU45cGd_bxm8E0Y")
    # Диспетчер для бота
    dp = Dispatcher(bot)
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)


    # Хэндлер на команду /test1
    @dp.message_handler(commands="test1")
    async def cmd_test1(message: types.Message):
        await message.reply("Test 1")


    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
