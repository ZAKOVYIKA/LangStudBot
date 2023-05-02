import webhook.Chat_Routines.creating_buttons_routines as cbr
import webhook.Chat_Routines.chatDictiRoutines.dicti_buttons_routines as dbr
import webhook.DB_Routines.Dict_routines as Dr
import webhook.DB_Routines.WCtg_routines as WCr
import webhook.DB_Routines.User_routines as Ur
import random
import telebot

hide_keyboard = telebot.types.ReplyKeyboardRemove()

def main_page(message, bot):
    keyboard = dbr.dicti_menu()
    bot.send_message(message.chat.id, f'Вот словарик! Что делаем?', parse_mode = 'HTML', reply_markup = keyboard)
    bot.register_next_step_handler(message, chose_dicti, bot)
# end

def chose_dicti(message, bot):
    if message.text == "Искать слово":
        keyboard = dbr.dicti_back_button()
        bot.send_message(message.chat.id, 'Введи слово на русском или английском языке', parse_mode='HTML', reply_markup = keyboard)
        bot.register_next_step_handler(message, find_word, bot)

    elif message.text == 'Искать категорию':
        keyboard = dbr.dicti_back_button()
        bot.send_message(message.chat.id, 'Введи искомую категорию или часть её названия', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, find_catg, bot)

    elif message.text == "Вывести все слова из категории":
        bot.send_message(message.chat.id, 'Введи категорию, из которой ты хочешь вывести все слова. \n Вот небольшая подсказка от меня.', parse_mode='HTML', reply_markup=hide_keyboard)
        all_catg_in(message, bot)
        bot.register_next_step_handler(message, all_words_catg, bot)

    elif message.text == "Вывести все категории":
        keyboard = dbr.dicti_menu()
        bot.send_message(message.chat.id, 'Нет проблем!', parse_mode='HTML', reply_markup=keyboard)
        all_catg_in(message, bot)
        bot.register_next_step_handler(message, chose_dicti, bot)

    elif message.text == "Добавить/Удалить/Изменить слово":
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, 'Принято', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'w')

    elif message.text == "Добавить/Удалить/Изменить категорию":
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, 'Принято', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'c')

    elif message.text == "Назад":
        keyboard = cbr.main_menu()
        bot.send_message(message.chat.id, 'Хорошо', parse_mode='HTML', reply_markup=keyboard)

    else:
        keyboard = dbr.dicti_menu()
        bot.send_message(message.chat.id, f'Увы, я не знаю такой команды... \n'
                                          f'Попробуй использовать кнопки.', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_dicti, bot)
    # end
# end

def find_word(message, bot):
    user = Ur.db_read(message.from_user.id)

    w = Dr.db_search_word(word = message.text, uid = user)
    if w is None:
        keyboard = dbr.dicti_back_button()
        bot.send_message(message.chat.id, 'Что-то ничего нашлось. Попробуй ещё разок.', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, check_find_word, bot)
    else:
        keyboard = dbr.dicti_back_button()
        ans = f'Смотри, вот что мне удалось найти:\n'
        for word in w:
            ans = ans + f'{word}\n'
        # end
        bot.send_message(message.chat.id, f'{ans}', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, check_find_word, bot)
    # end
# end

def check_find_word(message, bot):
    if message.text == 'Назад':
        keyboard = dbr.dicti_menu()
        bot.send_message(message.chat.id, f'Хорошо', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_dicti, bot)
    else:
        find_word(message, bot)
    # end
# end

def find_catg(message, bot):
    user = Ur.db_read(message.from_user.id)

    c = WCr.db_search_name(name=message.text, uid=user)
    print(c)
    if c is None:
        keyboard = dbr.dicti_back_button()
        bot.send_message(message.chat.id, 'Что-то категорий нашлось. Попробуй ещё разок.', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, check_find_catg, bot)
    else:
        keyboard = dbr.dicti_back_button()
        ans = f'Смотри, вот все категории для слов:\n'
        for catg in c:
            ans = ans + f'{catg}\n'
        # end


        bot.send_message(message.chat.id, ans, parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, check_find_catg, bot)
    # end
# end

def check_find_catg(message, bot):
    if message.text == 'Назад':
        keyboard = dbr.dicti_menu()
        bot.send_message(message.chat.id, f'Хорошо', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_dicti, bot)
    else:
        find_catg(message, bot)
    # end
# end

def all_catg_in(message, bot):
    user = Ur.db_read(message.from_user.id)

    c = WCr.db_read_uid(uid=user)
    if c is None:
        bot.send_message(message.chat.id, 'Что-то ничего не нашлось. Попробуй ещё разок.', parse_mode='HTML')
    else:
        ans = f'Смотри, что мне удалось найти:\n'
        for catg in c:
            ans = ans + '<u>'+f'{catg}\n' + '</u>'
        # end
        bot.send_message(message.chat.id, ans, parse_mode='HTML')
    # end
# end

def all_words_catg(message, bot):
    user = Ur.db_read(message.from_user.id)
    catg = WCr.db_read_name(name = message.text, uid = user)
    print (catg)
    if catg is None:
        keyboard = dbr.dicti_menu()
        bot.send_message(message.chat.id, f'Или у нас нет категорий, или ты что-то ввёл не так. \n Попробуй снова', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_dicti, bot)
    # end

    w = Dr.db_read_catg(wordcatg = catg[0], uid = user)
    print(w)
    if w is None:
        keyboard = dbr.dicti_menu()
        bot.send_message(message.chat.id, 'Что-то ничего нашлось. Попробуй ещё разок.', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_dicti, bot)
    else:
        keyboard = dbr.dicti_menu()
        ans = f'Смотри, вот все слова из категории <u>{catg[0].Name}</u>:\n'
        for word in w:
            ans = ans + f'{word}\n'
        # end
        bot.send_message(message.chat.id, f'{ans}', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_dicti, bot)
    # end
# end

def chose_cud(message, bot, flag):
    print(message.text)
    if message.text == 'Добавить':
        if flag == 'w':
            bot.send_message(message.chat.id, f'Хорошо. Введи слово из <u>русского</u> языка', parse_mode='HTML', reply_markup=hide_keyboard)
            bot.register_next_step_handler(message, add_word_1, bot)
        elif flag == 'c':
            bot.send_message(message.chat.id, f'Хорошо. Введи название категории', parse_mode='HTML',
                             reply_markup=hide_keyboard)
            bot.register_next_step_handler(message, add_catg_1, bot)
        else:
            keyboard = dbr.dicti_menu()
            bot.send_message(message.chat.id, f'Ой-ой-ой, что пошло не так!', parse_mode='HTML', reply_markup=keyboard)
            bot.register_next_step_handler(message, chose_dicti, bot)
        # end
    elif message.text == 'Изменить':
        if flag == 'w':
            bot.send_message(message.chat.id, f'Хорошо. Введи слово из <u>иностранного</u> языка, параметры которого ты хочешь поменять', parse_mode='HTML',
                             reply_markup=hide_keyboard)
            bot.register_next_step_handler(message, update_word_1, bot)
        elif flag == 'c':
            bot.send_message(message.chat.id,
                             f'Хорошо. Введи имя категории',
                             parse_mode='HTML',
                             reply_markup=hide_keyboard)
            bot.register_next_step_handler(message, update_catg_1, bot)
        else:
            keyboard = dbr.dicti_menu()
            bot.send_message(message.chat.id, f'Ой-ой-ой, что пошло не так!', parse_mode='HTML', reply_markup=keyboard)
            bot.register_next_step_handler(message, chose_dicti, bot)
        # end
    elif message.text == 'Удалить':
        if flag == 'w':
            bot.send_message(message.chat.id, f'Хорошо. Введи слово из <u>иностранного</u> языка', parse_mode='HTML',
                             reply_markup=hide_keyboard)
            bot.register_next_step_handler(message, delete_word_1, bot)
        elif flag == 'c':
            bot.send_message(message.chat.id, f'Учти, вместе с категорией будут удалены все слова! \n Введи имя категории', parse_mode='HTML',
                             reply_markup=hide_keyboard)
            bot.register_next_step_handler(message, delete_catg_1, bot)
        else:
            keyboard = dbr.dicti_menu()
            bot.send_message(message.chat.id, f'Ой-ой-ой, что пошло не так!', parse_mode='HTML', reply_markup=keyboard)
            bot.register_next_step_handler(message, chose_dicti, bot)
        # end

    elif message.text == "Назад":
        keyboard = dbr.dicti_menu()
        bot.send_message(message.chat.id, f'Хорошо', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_dicti, bot)

    else:
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'Увы, я не знаю такой команды... \n'
                                          f'Попробуй использовать кнопки.', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, flag)
    # end
# end

def update_catg_1(message, bot):
    user = Ur.db_read(message.from_user.id)

    name = message.text

    dbid = WCr.db_id(name=name, uid=user)
    print(dbid)
    if dbid is None:
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'А такой категории нет', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'c')
    else:
        keyboard = dbr.dicti_ctgupd_menu()
        bot.send_message(message.chat.id, f'Что именно ты хочешь поменять?', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, update_catg_2_menu, bot, dbid[0])
    # end
# end

def update_catg_2_menu(message, bot, dbid):
    if message.text == 'Изменить название категории':
        bot.send_message(message.chat.id, f'Хорошо. Введи новое название:', parse_mode='HTML', reply_markup=hide_keyboard)
        bot.register_next_step_handler(message, update_catg_3_name, bot, dbid)

    elif message.text == 'Назад':
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'Хорошо', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'c')
    else:
        keyboard = dbr.dicti_ctgupd_menu()
        bot.send_message(message.chat.id, f'Такой команды нет. Попробуй использовать кнопки.', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, update_catg_2_menu, bot, dbid)
    # end
# end

def update_catg_3_name(message, bot, dbid):
    user = Ur.db_read(message.from_user.id)

    name = message.text
    print(dbid)
    res = WCr.db_update(ctgid = dbid, new_name = name, uid = user)

    if res is not None:
        keyboard = dbr.dicti_ctgupd_menu()
        bot.send_message(message.chat.id, f'Обновление прошло успешно! Что-то ещё?', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, update_catg_2_menu, bot, dbid)
    else:
        keyboard = dbr.dicti_ctgupd_menu()
        bot.send_message(message.chat.id, f'Что-то пошло не так. Попробуй ещё.', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, update_catg_2_menu, bot, dbid)
    # end
# end

def delete_catg_1(message, bot):
    user = Ur.db_read(message.from_user.id)

    name = message.text
    dbid = WCr.db_id(name = name, uid = user)
    print(dbid)
    if dbid is None:
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'А такой категории и не было...', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'c')
    else:
        res = WCr.db_delete(ctgid = dbid[0], uid = user)
        print(res)
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'Категория успешно удалена!', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'c')
    # end
# end

def add_catg_1(message, bot):
    user = Ur.db_read(message.from_user.id)

    name = message.text
    res = WCr.db_read_name(name = name, uid = user)

    if res is not None:
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'Такая категория уже есть. Не стоит засорять словарик.', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'c')
    else:
        res = WCr.db_create(name = name, uid = user)
        if res is not None:
            keyboard = dbr.dicti_cud_menu()
            bot.send_message(message.chat.id, f'Создание категории прошло успешно!', parse_mode='HTML',
                             reply_markup=keyboard)
            bot.register_next_step_handler(message, chose_cud, bot, 'c')
        else:
            keyboard = dbr.dicti_cud_menu()
            bot.send_message(message.chat.id, f'Что-то пошло не так!', parse_mode='HTML',
                             reply_markup=keyboard)
            bot.register_next_step_handler(message, chose_cud, bot, 'c')
        # end
    # end
# end


def update_word_1(message, bot):
    user = Ur.db_read(message.from_user.id)

    wf = message.text

    dbid = Dr.db_id(word=wf, uid=user)
    if dbid is None:
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'А такого слова нет', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'w')
    else:
        keyboard = dbr.dicti_wupd_menu()
        bot.send_message(message.chat.id, f'Что именно ты хочешь поменять?', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, update_word_2_menu, bot, dbid[0])
    # end
# end

def update_word_2_menu(message, bot, dbid):
    if message.text == 'Изменить русский перевод':
        bot.send_message(message.chat.id, f'Хорошо. Введи новый перевод:', parse_mode='HTML', reply_markup=hide_keyboard)
        bot.register_next_step_handler(message, update_word_3_wr, bot, dbid)
    elif message.text == 'Изменить иностранное слово':
        bot.send_message(message.chat.id, f'Хорошо. Введи новый исходник:', parse_mode='HTML',
                         reply_markup=hide_keyboard)
        bot.register_next_step_handler(message, update_word_3_wf, bot, dbid)
    elif message.text == 'Изменить категорию':
        bot.send_message(message.chat.id, f'Хорошо. Введи новую категорию:', parse_mode='HTML',
                         reply_markup=hide_keyboard)
        bot.register_next_step_handler(message, update_word_3_c, bot, dbid)
    elif message.text == 'Назад':
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'Хорошо', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'w')
    else:
        keyboard = dbr.dicti_wupd_menu()
        bot.send_message(message.chat.id, f'Такой команды нет. Попробуй использовать кнопки.', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, update_word_2_menu, bot, dbid)
    # end
# end

def update_word_3_wr(message, bot, dbid):
    user = Ur.db_read(message.from_user.id)
    print(dbid)
    wr = message.text
    print(wr)
    res = Dr.db_update(wid = dbid, new_wr = wr, uid = user)
    print(res)
    if res is not None:
        keyboard = dbr.dicti_wupd_menu()
        bot.send_message(message.chat.id, f'Обновление прошло успешно! Что-то ещё?', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, update_word_2_menu, bot, dbid)
    else:
        keyboard = dbr.dicti_wupd_menu()
        bot.send_message(message.chat.id, f'Что-то пошло не так. Попробуй ещё.', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, update_word_2_menu, bot, dbid)
    # end

# end

def update_word_3_wf(message, bot, dbid):
    user = Ur.db_read(message.from_user.id)

    wf = message.text
    res = Dr.db_read_word(word = wf, uid = user)
    if res is not None:
        keyboard = dbr.dicti_wupd_menu()
        bot.send_message(message.chat.id, f'Такое слово уже есть', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, update_word_2_menu, bot, dbid)
    else:
        res = Dr.db_update(wid=dbid, new_wf = wf, uid=user)
        if res is not None:
            keyboard = dbr.dicti_wupd_menu()
            bot.send_message(message.chat.id, f'Обновление прошло успешно! Что-то ещё?', parse_mode='HTML',
                             reply_markup=keyboard)
            bot.register_next_step_handler(message, update_word_2_menu, bot, dbid)
        else:
            keyboard = dbr.dicti_wupd_menu()
            bot.send_message(message.chat.id, f'Что-то пошло не так. Попробуй ещё.', parse_mode='HTML',
                             reply_markup=keyboard)
            bot.register_next_step_handler(message, update_word_2_menu, bot, dbid)
        # end
    # end
# end

def update_word_3_c(message, bot, dbid):
    user = Ur.db_read(message.from_user.id)

    # Считали категорию на русском
    catg = message.text
    # Проверили, что такой записи ещё нет
    c = WCr.db_read_name(name=catg, uid=user)

    if c is None:
        keyboard = dbr.dicti_wupd_menu()
        bot.send_message(message.chat.id, f'Такой категори ещё нет. Сначала надо её создать отдельным действием.',
                         parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, update_word_2_menu, bot, dbid)
    else:
        res = Dr.db_update(wid=dbid, new_catg=c[0], uid=user)
        if res is not None:
            keyboard = dbr.dicti_wupd_menu()
            bot.send_message(message.chat.id, f'Обновление прошло успешно! Что-то ещё?', parse_mode='HTML',
                             reply_markup=keyboard)
            bot.register_next_step_handler(message, update_word_2_menu, bot, dbid)
        else:
            keyboard = dbr.dicti_wupd_menu()
            bot.send_message(message.chat.id, f'Что-то пошло не так. Попробуй ещё.', parse_mode='HTML',
                             reply_markup=keyboard)
            bot.register_next_step_handler(message, update_word_2_menu, bot, dbid)
        # end
    # end
# end


def delete_word_1(message, bot):
    user = Ur.db_read(message.from_user.id)

    wf = message.text

    dbid = Dr.db_id(word = wf, uid = user)
    if dbid is None:
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'А такого слова и не было...', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'w')
    else:
        Dr.db_delete(wid = dbid[0], uid = user)
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'Слово успешно удалено!', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'w')
    # end
# end

def add_word_1(message, bot):
    wr = message.text
    bot.send_message(message.chat.id, f'Введи слово из <u>иностранного</u> языка', parse_mode='HTML',
                     reply_markup=hide_keyboard)
    bot.register_next_step_handler(message, add_word_2, bot, wr)
# end

def add_word_2(message, bot, wr):
    user = Ur.db_read(message.from_user.id)
    # Считали слово на русском
    wf = message.text
    # Проверили, что такой записи ещё нет
    w = Dr.db_read_word(word = wf, uid = user)

    if w is not None:
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'Такое слово уже было. Не стоит засорять словарик.', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'w')
    else:
        bot.send_message(message.chat.id, f'Введи название категории, к которому будет относиться это слово', parse_mode='HTML',
                     reply_markup=hide_keyboard)
        bot.register_next_step_handler(message, add_word_3, bot, wr, wf)
    # end
# end

def add_word_3(message, bot, wr, wf):
    user = Ur.db_read(message.from_user.id)
    # Считали категорию на русском
    catg = message.text
    # Проверили, что такой записи ещё нет
    c = WCr.db_read_name(name=catg, uid=user)

    if c is None:
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'Такой категори ещё нет. Сначала надо её создать отдельным действием.', parse_mode='HTML',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'w')
    else:
        Dr.db_create(uid = user, WordRussian = wr, WordForeign = wf, catg = c[0])
        keyboard = dbr.dicti_cud_menu()
        bot.send_message(message.chat.id, f'Слово успешно записано!',
                     parse_mode='HTML',
                     reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_cud, bot, 'w')
    # end
# end