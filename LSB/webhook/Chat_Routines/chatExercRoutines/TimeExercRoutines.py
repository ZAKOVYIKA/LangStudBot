import webhook.Chat_Routines.chatExercRoutines.exerc_buttons_routines as ebr
import webhook.Chat_Routines.chatExercRoutines.chatExerc_routine as cEr
import webhook.DB_Routines.Exerc_routines as Er
import webhook.DB_Routines.RECtg_routines as RECr
import random
import telebot

hide_keyboard = telebot.types.ReplyKeyboardRemove()

def chose_time(message, bot):
    print('Мы в choose_time')
    if message.text in ['Past', 'Present', 'Future']:
        keyboard = ebr.exerc_exac_times_menu()
        bot.send_message(message.chat.id, 'Выбери конкретное время', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_exac_time, bot, message.text)

    elif message.text == 'Все':
        bot.send_message(message.chat.id, 'Ого! Круто! \n Выведу тебе все задачи, что у меня есть! :)', parse_mode='HTML', reply_markup=hide_keyboard)
        get_exac_time_exerc(message, bot, ['Past', 'Present', 'Future'], 1)

    elif message.text == "Назад":
        keyboard = ebr.exerc_menu()
        bot.send_message(message.chat.id, 'Хорошо', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, cEr.chose_exerc, bot)

    else:
        keyboard = ebr.exerc_times_menu()
        bot.send_message(message.chat.id, f'Увы, я не знаю такой команды... \n'
                                          f'Попробуй использовать кнопки.', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_time, bot)
    # end
# end

def chose_exac_time(message, bot, time):
    print('Мы в chose_exac_time')
    if message.text in ['Simple', 'Continous', 'Perfect', 'Perfect Continous']:
        print(time)
        get_exac_time_exerc(message, bot, time + ' ' + message.text, 0)

    elif message.text == 'Все':
        bot.send_message(message.chat.id, f'Отличный выбор! \n Выведу тебе все задачи по {time}, что у меня есть! :)', parse_mode='HTML', reply_markup=hide_keyboard)
        get_exac_time_exerc(message, bot, time, 2)

    elif message.text == "Назад":
        keyboard = ebr.exerc_times_menu()
        bot.send_message(message.chat.id, 'Хорошо', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_time, bot)

    else:
        keyboard = ebr.exerc_exac_times_menu()
        bot.send_message(message.chat.id, f'Увы, я не знаю такой команды... \n'
                                          f'Попробуй использовать кнопки.', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_exac_time, bot)
    # end
# end

def get_exac_time_exerc(message, bot, exactime, flag):
    print('Мы в get_exac_time_exerc')
    # Если упражнения только на одно время
    if flag == 0:
        print('Мы в get_exac_time_exerc 0')
        catg = RECr.db_read(exactime)
        print(catg)
        if catg is None:
            keyboard = ebr.exerc_times_menu()
            bot.send_message(message.chat.id, f'Увы, для такого времени задание мы ещё не придумали :( \n Следи за обновлениями! :)', parse_mode='HTML', reply_markup=keyboard)
            bot.register_next_step_handler(message, chose_time, bot)
        # end
        ansExerc = Er.db_read_catg(exerccatg = catg[0])
        print(ansExerc)
    # Если запрос на упражнения на все времена
    elif flag == 1:
        print('Мы в get_exac_time_exerc 1')
        catg = []
        for time in exactime:
            tcatg = RECr.db_name_search(time)
            print(time)
            print(tcatg)
            if tcatg is None:
                bot.send_message(message.chat.id,
                                 f'Увы, для {time} времени задание мы ещё не придумали :( \n Следи за обновлениями! :)',
                                 parse_mode='HTML')
            else:
                catg = [*catg, *tcatg]
            # end
        # end

        if catg == []:
            keyboard = ebr.exerc_times_menu()
            bot.send_message(message.chat.id, f'Увы, мы вообще задания на времена не придумали :( \n Следи за обновлениями! :)', parse_mode='HTML', reply_markup=keyboard)
            bot.register_next_step_handler(message, chose_time, bot)
        # end

        ansExerc = []
        for ctg in catg:
            tExerc = Er.db_read_catg(exerccatg = ctg)
            if tExerc is None:
                bot.send_message(message.chat.id,
                                 f'Увы, для {ctg.Name} времени задание мы ещё не придумали :( \n Следи за обновлениями! :)',
                                 parse_mode='HTML')
            else:
                ansExerc = [*ansExerc, *tExerc]
            # end
        # end

        if ansExerc == []:
            keyboard = ebr.exerc_times_menu()
            bot.send_message(message.chat.id, f'Увы, мы вообще задания на времена не придумали :( \n Следи за обновлениями! :)', parse_mode='HTML', reply_markup=keyboard)
            bot.register_next_step_handler(message, chose_time, bot)
        # end

    # Если упраженния на все типы одного времени
    elif flag == 2:
        print('Мы в get_exac_time_exerc 2')
        catg = RECr.db_name_search(exactime)
        if catg is None:
            keyboard = ebr.exerc_times_menu()
            bot.send_message(message.chat.id,
                                 f'Увы, для {exactime} времени задание мы ещё не придумали :( \n Следи за обновлениями! :)',
                                 parse_mode='HTML', reply_markup=keyboard)
            bot.register_next_step_handler(message, chose_time, bot)
        # end

        ansExerc = []
        for ctg in catg:
            tExerc = Er.db_read_catg(exerccatg = ctg)
            if tExerc is None:
                bot.send_message(message.chat.id,
                                 f'Увы, для {ctg.Name} времени задание мы ещё не придумали :( \n Следи за обновлениями! :)',
                                 parse_mode='HTML')
            else:
                ansExerc = [*ansExerc, *tExerc]
            # end
        # end

        if ansExerc == []:
            keyboard = ebr.exerc_times_menu()
            bot.send_message(message.chat.id, f'Увы, мы вообще задания на времена не придумали :( \n Следи за обновлениями! :)', parse_mode='HTML', reply_markup=keyboard)
            bot.register_next_step_handler(message, chose_time, bot)
        # end
    else:
        keyboard = ebr.exerc_menu()
        bot.send_message(message.chat.id, 'Ой-ой-ой, что-то полшло не так!', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, cEr.chose_exerc, bot)
    # end

    print('Мы закончили get')
    start_exercise(message, bot, ansExerc)
# end

def start_exercise(message, bot, ansExerc):
    print('Мы в start_exercise')
    # Определили случайное задание
    exerc = random.choice(ansExerc)
    exerc = random.choice(ansExerc)
    bot.send_message(message.chat.id, 'Сейчас я отправлю задание. \n Тебе необходимо напечатать ответ и отправить его мне.', parse_mode='HTML', reply_markup = hide_keyboard)
    bot.send_message(message.chat.id, f'{exerc}', parse_mode='HTML', reply_markup = hide_keyboard)
    bot.register_next_step_handler(message, do_exercise, bot, exerc, ansExerc)

# end

def do_exercise(message, bot, exerc, ansExerc):
    ans = exerc.Answer
    ans = ans.lower()
    ans = ans.replace('\n', '')
    ans = ans.replace(',', '')
    ans = ans.replace(';', '')
    ans = ans.replace('.', '')
    ans = ans.replace(' ', '')

    msg = message.text.lower()
    msg = msg.replace('\n', '')
    msg = msg.replace(' ', '')
    msg = msg.replace(',', '')
    msg = msg.replace(';', '')
    msg = msg.replace('.', '')

    if  msg == ans:
        keyboard = ebr.exerc_next_task_menu()
        bot.send_message(message.chat.id,
                         'Правильно! \n Ещё задачку?',
                         parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, next_exercise, bot, ansExerc)
    elif msg == 'повторизадачу':
        bot.send_message(message.chat.id, f'{exerc}', parse_mode='HTML', reply_markup = hide_keyboard)
        bot.register_next_step_handler(message, do_exercise, bot, exerc, ansExerc)
    elif msg == 'сдаюсь':
        keyboard = ebr.exerc_next_task_menu()
        bot.send_message(message.chat.id,
                         f'Ну вот :( \n Ответ был такой: <tg-spoiler>{exerc.Answer}</tg-spoiler> \n Ещё задачку?',
                         parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, next_exercise, bot, ansExerc)
    else:
        keyboard = ebr.exerc_do_task_menu()
        bot.send_message(message.chat.id,
                         'Не-а, попробуй ещё',
                         parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, do_exercise, bot, exerc, ansExerc)
    # end
# end

def next_exercise(message, bot, ansExerc):
    if message.text == "Продолжим":
        start_exercise(message, bot, ansExerc)
    elif message.text == 'Достаточно':
        keyboard = ebr.exerc_menu()
        bot.send_message(message.chat.id, 'Хорошо', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, cEr.chose_exerc, bot)
    else:
        keyboard = ebr.exerc_next_task_menu()
        bot.send_message(message.chat.id,
                         f'Что-то не так. Попробуй использовать кнопки.',
                         parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, next_exercise, bot)
    # end
# end