import telebot

def rule_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    times_button = telebot.types.KeyboardButton("Времена")
    artic_button = telebot.types.KeyboardButton("Артикли")
    compl_button = telebot.types.KeyboardButton("Complex smth")
    exit_button = telebot.types.KeyboardButton('Назад')

    keyboard.row(times_button, artic_button, compl_button)
    keyboard.row(exit_button)

    return keyboard
# end


def rule_times_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    past_button = telebot.types.KeyboardButton("Past")
    present_button = telebot.types.KeyboardButton("Present")
    future_button = telebot.types.KeyboardButton("Future")
    exit_button = telebot.types.KeyboardButton('Назад')
    keyboard.row(past_button, present_button, future_button)
    keyboard.row(exit_button)

    return keyboard
# end

def rule_exac_times_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    simple_button = telebot.types.KeyboardButton("Simple")
    continous_button = telebot.types.KeyboardButton("Continous")
    perfect_button = telebot.types.KeyboardButton("Perfect")
    perfectcontinous_button = telebot.types.KeyboardButton("Perfect Continous")
    exit_button = telebot.types.KeyboardButton('Назад')
    keyboard.row(simple_button, continous_button)
    keyboard.row(perfect_button, perfectcontinous_button)
    keyboard.row(exit_button)

    return keyboard
# end
