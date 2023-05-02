import telebot
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import webhook.Chat_Routines.start_routine as SR
import webhook.Chat_Routines.help_routine as HR
import webhook.Chat_Routines.creating_buttons_routines as cbr
import webhook.Chat_Routines.chatRuleRoutines.chatRule_routine as cRr
import webhook.Chat_Routines.chatDictiRoutines.chatDicti_routine as cDr
import webhook.Chat_Routines.chatExercRoutines.chatExerc_routine as cEr

# Объявление переменной бота
bot = telebot.TeleBot(settings.TGBOTTOKEN)

#декоратор csrf – cross site reference cooky,
# обеспечивает дополнительную безопасность
@csrf_exempt
def webhook(request):
    ngrok_url = settings.NGROK_URL
    bot.set_webhook(ngrok_url)


    # проверка на то, какого типа пришел запрос
    if request.META["CONTENT_TYPE"] == "application/json":
        json_data = request.body.decode("utf-8")
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        # после того, как все обработали, возвращаем пустой элемент.
        # В рамках клиент-серверной архитектуры нужно
        # обязательно вернуть хоть что-то.
        return HttpResponse("")
    else:
        # ошибка 403. Мы таким образом защищаем
        # бота от разнообразных атак.
        raise PermissionDenied
    # end
# end

# Обрабатываем команду /start
@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    SR.start_routine(message, bot)
# end

# Обрабатываем команду /help
@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    HR.help_routine(message, bot)
# end

# Обрабатываем команду /button на вызов кнопок главного меню
@bot.message_handler(commands=['button'])
def button(message):
    keyboard = cbr.main_menu()
    bot.send_message(message.chat.id, 'Окей. Вот главное меню.', reply_markup = keyboard)
# end

# Обрабатываем основное меню
@bot.message_handler(content_types=['text'])
def main_text_processing(message):
    if message.text == "Правила":
        bot.send_message(message.chat.id, 'Ура! Учим правила!', parse_mode = 'HTML')
        cRr.main_page(message, bot)

    elif message.text == 'Упражнения':
        bot.send_message(message.chat.id, 'Repetitio est mater studiorum!', parse_mode = 'HTML')
        cEr.main_page(message, bot)

    elif message.text == "Словарь":
        bot.send_message(message.chat.id, 'Словарь? Сейчас будет!', parse_mode = 'HTML')
        cDr.main_page(message, bot)

    elif message.text == "Статистика":
        keyboard = cbr.main_menu()
        bot.send_message(message.chat.id, 'Так-с, так-с, так-с... \n А статистику мы пока ещё не сделали :(', parse_mode = 'HTML', reply_markup = keyboard)

    else:
        keyboard = cbr.main_menu()
        bot.send_message(message.chat.id, f'Увы, я не знаю такой команды... \n'
                                          f'Попробуй использовать кнопки или специальные команды из /help.', parse_mode = 'HTML', reply_markup = keyboard)
    # end
# end