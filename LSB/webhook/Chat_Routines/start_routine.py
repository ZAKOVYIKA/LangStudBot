import webhook.DB_Routines.Rule_routines as Rr
import webhook.DB_Routines.Exerc_routines as Er
import webhook.DB_Routines.RECtg_routines as RECr
import webhook.DB_Routines.Dict_routines as Dr
import webhook.DB_Routines.User_routines as Ur
import webhook.DB_Routines.WCtg_routines as WCr
from webhook.models import Rule, RECategory, Exercise
import webhook.Chat_Routines.creating_buttons_routines as cbr

def start_routine(message, bot):
    bot.send_message(message.chat.id, f'Загрузка...', parse_mode='HTML')

    # Определили пользователя
    Ur.db_create(uid=message.from_user.id)
    username = message.from_user.username
    user = Ur.db_read(message.from_user.id)

    Rr.db_delete_all()
    Er.db_delete_all()
    RECr.db_delete_all()
    Dr.db_delete_all(uid = user)
    WCr.db_delete_all(uid = user)

    if len(Rule.objects.all()) == 0:
        Rr.db_initialize('iniRuleDB.txt')
        print('Ининциализорована новая БД правил')
    # end
    if len(Exercise.objects.all()) == 0:
        Er.db_initialize('iniExercDB.txt')
        print('Ининциализорована новая БД упражнений')
    # end

    # Активируем кнопочки
    keyboard = cbr.main_menu()

    #Определили пользователя
    Ur.db_create(uid = message.from_user.id)
    username = message.from_user.username
    user = Ur.db_read(message.from_user.id)

    # Составили приветствие c активацией кнопочек
    str1 = f'Привет, @{username}! \n'
    str2 = f'Рады <b>тебя</b> видеть в нашем обучающем боте! \n'
    str3 = f'Чтобы получить больше информации о возможностях бота просто введи /help или приступай к исследованию самостоятельно, нажимая кнопки! \n'
    str4 = f'Удачи в изучении языков!'
    ansstr = str1 + str2 + str3 + str4
    bot.send_message(message.chat.id, ansstr, parse_mode = 'HTML', reply_markup = keyboard)

# end