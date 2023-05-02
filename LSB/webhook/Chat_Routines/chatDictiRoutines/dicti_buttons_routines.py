import telebot


def dicti_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    findword_button = telebot.types.KeyboardButton("Искать слово")
    findcatg_button = telebot.types.KeyboardButton("Искать категорию")
    allincatg_button = telebot.types.KeyboardButton("Вывести все слова из категории")
    allcatg_button = telebot.types.KeyboardButton("Вывести все категории")
    cudword_button = telebot.types.KeyboardButton("Добавить/Удалить/Изменить слово")
    cudcatg_button = telebot.types.KeyboardButton("Добавить/Удалить/Изменить категорию")
    exit_button = telebot.types.KeyboardButton('Назад')

    keyboard.row(findword_button, findcatg_button)
    keyboard.row(allincatg_button, allcatg_button)
    keyboard.add(cudword_button)
    keyboard.add(cudcatg_button)
    keyboard.row(exit_button)

    return keyboard
# end

def dicti_back_button():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    exit_button = telebot.types.KeyboardButton('Назад')
    keyboard.row(exit_button)

    return keyboard
# end

def dicti_cud_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    create_button = telebot.types.KeyboardButton("Добавить")
    update_button = telebot.types.KeyboardButton("Изменить")
    delete_button = telebot.types.KeyboardButton("Удалить")
    exit_button = telebot.types.KeyboardButton('Назад')

    keyboard.row(create_button, update_button)
    keyboard.row(delete_button)
    keyboard.row(exit_button)

    return keyboard
# end

def dicti_wupd_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    uwr_button = telebot.types.KeyboardButton("Изменить русский перевод")
    uwf_button = telebot.types.KeyboardButton("Изменить иностранное слово")
    uc_button = telebot.types.KeyboardButton("Изменить категорию")
    exit_button = telebot.types.KeyboardButton('Назад')

    keyboard.row(uwr_button)
    keyboard.add(uwf_button)
    keyboard.row(uc_button)
    keyboard.row(exit_button)

    return keyboard
# end

def dicti_ctgupd_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    ucn_button = telebot.types.KeyboardButton("Изменить название категории")
    exit_button = telebot.types.KeyboardButton('Назад')

    keyboard.row(ucn_button)
    keyboard.row(exit_button)

    return keyboard
# end