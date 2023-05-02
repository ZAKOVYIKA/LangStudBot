import webhook.Chat_Routines.creating_buttons_routines as cbr
import webhook.Chat_Routines.chatExercRoutines.exerc_buttons_routines as ebr
import webhook.Chat_Routines.chatExercRoutines.TimeExercRoutines as TER

def main_page(message, bot):
    keyboard = ebr.exerc_menu()
    bot.send_message(message.chat.id, f'Итак, выбери тему, по которой ты бы хотел позаниматься', parse_mode = 'HTML', reply_markup = keyboard)
    bot.register_next_step_handler(message, chose_exerc, bot)
# end

def chose_exerc(message, bot):
    if message.text == "Времена":
        keyboard = ebr.exerc_times_menu()
        bot.send_message(message.chat.id, 'Выбери конкретное время', parse_mode='HTML', reply_markup = keyboard)
        bot.register_next_step_handler(message, TER.chose_time, bot)

    elif message.text == 'Артикли':
        keyboard = ebr.exerc_menu()
        bot.send_message(message.chat.id, 'Увы, пока тут пусто... :( \n Следи за обновлениями! :)', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_exerc, bot)

    elif message.text == "Complex smth":
        keyboard = ebr.exerc_menu()
        bot.send_message(message.chat.id, 'Увы, пока тут пусто... :( \n Следи за обновлениями! :)', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_exerc, bot)

    elif message.text == "Назад":
        keyboard = cbr.main_menu()
        bot.send_message(message.chat.id, 'Хорошо', parse_mode='HTML', reply_markup=keyboard)

    else:
        keyboard = ebr.exerc_menu()
        bot.send_message(message.chat.id, f'Увы, я не знаю такой команды... \n'
                                          f'Попробуй использовать кнопки.', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_exerc, bot)
    # end
# end