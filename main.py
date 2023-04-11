# Чат-бот присылающий курс доллара если он выйдет за заданные границы (2 границы верхняя и нижняя) (+парсинг)

import bot
import parsecourse

if __name__ == "__main__":
    course_usd = parsecourse.course()
    bot.botfunc(course_usd)
