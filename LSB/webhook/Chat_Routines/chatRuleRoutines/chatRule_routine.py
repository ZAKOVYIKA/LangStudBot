import webhook.Chat_Routines.creating_buttons_routines as cbr
import webhook.Chat_Routines.chatRuleRoutines.rules_buttons_routines as rbr
import webhook.Chat_Routines.chatRuleRoutines.TimeRuleRoutines as TRR

def main_page(message, bot):
    keyboard = rbr.rule_menu()
    bot.send_message(message.chat.id, f'Итак, выбери тему, по которой ты бы хотел узнать правила', parse_mode = 'HTML', reply_markup = keyboard)
    bot.register_next_step_handler(message, chose_rule, bot)
# end

def chose_rule(message, bot):
    if message.text == "Времена":
        keyboard = rbr.rule_times_menu()
        bot.send_message(message.chat.id, 'Выбери конкретное время', parse_mode='HTML', reply_markup = keyboard)
        bot.register_next_step_handler(message, TRR.chose_time, bot)

    elif message.text == 'Артикли':
        keyboard = rbr.rule_menu()
        bot.send_message(message.chat.id, 'Увы, пока тут пусто... :( \n Следи за обновлениями! :)', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_rule, bot)

    elif message.text == "Complex smth":
        keyboard = rbr.rule_menu()
        bot.send_message(message.chat.id, 'Увы, пока тут пусто... :( \n Следи за обновлениями! :)', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_rule, bot)

    elif message.text == "Назад":
        keyboard = cbr.main_menu()
        bot.send_message(message.chat.id, 'Хорошо', parse_mode='HTML', reply_markup=keyboard)

    else:
        keyboard = rbr.rule_menu()
        bot.send_message(message.chat.id, f'Увы, я не знаю такой команды... \n'
                                          f'Попробуй использовать кнопки.', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_rule, bot)
    # end
# end

