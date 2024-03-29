import logging
from aiogram import Bot, Dispatcher, executor, types

pending_upper = False
pending_lower = False
change_borders = False


def botfunc(mean):
    bot = Bot(token="6277453202:AAGydD69wQ-ZkJnWTce5MU45cGd_bxm8E0Y")
    # Диспетчер для бота
    dp = Dispatcher(bot)
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)
    user = ['', '100', '70']

    @dp.message_handler(commands=['start'], state='*')
    async def start(msg: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text="/borders")
        button_2 = types.KeyboardButton(text="/info")
        keyboard.add(button_1)
        keyboard.add(button_2)
        await msg.answer("Бот покажет вам актуальный курс доллара, если он выйдет за границу. "
                         "Чтобы задать границы напишите команду /borders. "
                         "/info, если вы уже задавали границы ранее", reply_markup=keyboard)

    @dp.message_handler(commands=['info'])
    async def info(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["/upper", "/lower"]
        keyboard.add(*buttons)
        global change_borders
        user[0] = str(message.from_user.id)
        base_id = []
        file = open("users.txt", "r")
        base = file.readlines()
        file.close()
        for i in range(len(base)):
            base_id.append(base[i].split()[0])
        try:
            user_info = base[base_id.index(user[0])].split()
        except:
            user_info = []
        if int(user[1]) <= int(user[2]):
            await message.answer("Верхняя граница не может быть меньше нижней!", reply_markup=keyboard)
            return 0
        if (user[0] not in base_id) or change_borders:
            if user[0] != '' and user[1] != '' and user[2] != '':
                if user[0] not in base_id:
                    base.append(user[0] + " " + user[1] + " " + user[2])
                    base.append('\n')
                    base_id.append(user[0])
                else:
                    id_index = base_id.index(user[0])
                    base[id_index] = user[0] + " " + user[1] + " " + user[2] + "\n"
                file = open('users.txt', 'w')
                for count in range(len(base)):
                    file.write(base[count])
                file.close()
                user_info = base[base_id.index(user[0])].split()
                await message.answer("Верхняя граница " + user_info[1] + "\nНижняя граница " + user_info[2], reply_markup=keyboard)
            else:
                await message.answer("Задайте границы!", reply_markup=keyboard)
        else:
            await message.answer("Верхняя граница " + user_info[1] + "\nНижняя граница " + user_info[2], reply_markup=keyboard)
        if int(user_info[1]) > mean > int(user_info[2]):
            await bot.send_message(user[0], "Курс в пределах границы")
        else:
            await bot.send_message(user[0], "Курс вышел за границу " + str(mean))

    @dp.message_handler(commands=["borders"])
    async def borders(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["/upper", "/lower", "/info"]
        keyboard.add(*buttons)
        await message.answer(
            "Чтобы задать границы напишите /upper и /lower,"
            " а после /info чтобы узнать и обновить информацию о заданных границах", reply_markup=keyboard)

    @dp.message_handler(commands=['upper'])
    async def upper(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["/lower", "/info"]
        keyboard.add(*buttons)
        await message.answer("Задайте верхнюю границу", reply_markup=keyboard)
        global pending_upper, pending_lower, change_borders
        pending_upper = True
        pending_lower = False
        change_borders = True

    @dp.message_handler(commands=['lower'])
    async def lower(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["/upper", "/info"]
        keyboard.add(*buttons)
        await message.answer("Задайте нижнюю границу", reply_markup=keyboard)
        global pending_lower, pending_upper, change_borders
        pending_lower = True
        pending_upper = False
        change_borders = True

    @dp.message_handler(content_types='text')
    async def border(value: types.Message):
        global pending_lower, pending_upper
        if pending_lower:
            user[2] = str(value.text)
            pending_lower = False
            return 0
        if pending_upper:
            user[1] = str(value.text)
            pending_upper = False
            return 0

    executor.start_polling(dp, skip_updates=True)
