import telebot

def exerc_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    times_button = telebot.types.KeyboardButton("Времена")
    artic_button = telebot.types.KeyboardButton("Артикли")
    compl_button = telebot.types.KeyboardButton("Complex smth")
    exit_button = telebot.types.KeyboardButton('Назад')

    keyboard.row(times_button, artic_button, compl_button)
    keyboard.row(exit_button)

    return keyboard
# end

def exerc_times_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    past_button = telebot.types.KeyboardButton("Past")
    present_button = telebot.types.KeyboardButton("Present")
    future_button = telebot.types.KeyboardButton("Future")
    all_button = telebot.types.KeyboardButton("Все")
    exit_button = telebot.types.KeyboardButton('Назад')
    keyboard.row(past_button, present_button)
    keyboard.row(future_button, all_button)
    keyboard.row(exit_button)

    return keyboard
# end

def exerc_exac_times_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    simple_button = telebot.types.KeyboardButton("Simple")
    continous_button = telebot.types.KeyboardButton("Continous")
    perfect_button = telebot.types.KeyboardButton("Perfect")
    perfectcontinous_button = telebot.types.KeyboardButton("Perfect Continous")
    all_button = telebot.types.KeyboardButton("Все")
    exit_button = telebot.types.KeyboardButton('Назад')
    keyboard.row(simple_button, continous_button)
    keyboard.row(perfect_button, perfectcontinous_button)
    keyboard.row(all_button)
    keyboard.row(exit_button)

    return keyboard
# end

def exerc_do_task_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    repeat_button = telebot.types.KeyboardButton("Повтори задачу")
    flee_button = telebot.types.KeyboardButton("Сдаюсь")
    keyboard.add(repeat_button)
    keyboard.add(flee_button)

    return keyboard
# end

def exerc_next_task_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    next_button = telebot.types.KeyboardButton("Продолжим")
    enougth_button = telebot.types.KeyboardButton("Достаточно")
    keyboard.row(next_button, enougth_button)

    return keyboard
# end