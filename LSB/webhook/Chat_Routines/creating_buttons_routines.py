import telebot
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import webhook.Chat_Routines.start_routine as SR

def main_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    rules_button = telebot.types.KeyboardButton("Правила")
    exerc_button = telebot.types.KeyboardButton("Упражнения")
    dicti_button = telebot.types.KeyboardButton("Словарь")
    stats_button = telebot.types.KeyboardButton("Статистика")
    keyboard.add(rules_button)
    keyboard.add(exerc_button)
    keyboard.add(dicti_button)
    keyboard.add(stats_button)

    return keyboard
# end

def stats_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    exit_button = telebot.types.KeyboardButton('Назад')

    keyboard.add(exit_button)

    return keyboard
# end


