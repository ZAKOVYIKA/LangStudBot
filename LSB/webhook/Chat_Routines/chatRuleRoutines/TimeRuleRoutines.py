import webhook.Chat_Routines.chatRuleRoutines.rules_buttons_routines as rbr
import webhook.Chat_Routines.chatRuleRoutines.chatRule_routine as cRr
import webhook.DB_Routines.Rule_routines as Rr
import webhook.DB_Routines.RECtg_routines as RECr

def chose_time(message, bot):
    if message.text in ['Past', 'Present', 'Future']:
        keyboard = rbr.rule_exac_times_menu()
        bot.send_message(message.chat.id, 'Выбери конкретное время', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_exac_time, bot, message.text)

    elif message.text == "Назад":
        keyboard = rbr.rule_menu()
        bot.send_message(message.chat.id, 'Хорошо', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, cRr.chose_rule, bot)

    else:
        keyboard = rbr.rule_times_menu()
        bot.send_message(message.chat.id, f'Увы, я не знаю такой команды... \n'
                                          f'Попробуй использовать кнопки.', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_time, bot)
    # end
# end

def chose_exac_time(message, bot, time):
    if message.text in ['Simple', 'Continous', 'Perfect', 'Perfect Continous']:
        print(time)
        get_exac_time_rule(message, bot, time + ' ' + message.text)

    elif message.text == "Назад":
        keyboard = rbr.rule_times_menu()
        bot.send_message(message.chat.id, 'Хорошо', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_time, bot)

    else:
        keyboard = rbr.rule_exac_times_menu()
        bot.send_message(message.chat.id, f'Увы, я не знаю такой команды... \n'
                                          f'Попробуй использовать кнопки.', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_exac_time, bot)
    # end
# end

def get_exac_time_rule(message, bot, exactime):
    catg = RECr.db_read(exactime)
    if catg is None:
        keyboard = rbr.rule_times_menu()
        bot.send_message(message.chat.id, f'Увы, такое правило мы ещё не записали :( \n Следи за обновлениями! :)', parse_mode='HTML', reply_markup=keyboard)
        bot.register_next_step_handler(message, chose_time, bot)
    # end
    ansRule = Rr.db_read_catg(rulecatg = catg[0])
    keyboard = rbr.rule_times_menu()
    bot.send_message(message.chat.id, f'{ansRule}', parse_mode='HTML', reply_markup=keyboard)
    bot.register_next_step_handler(message, chose_time, bot)
# end