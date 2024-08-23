import os
import telebot
from telebot import types

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

#
# @bot.message_handler(commands=["start", "hello"])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")
#
#
# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


@bot.message_handler(commands=["start"])
def send_hello(message):
    # Создаем клавиатуру с одной кнопкой "Начать"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("Начать")
    markup.add(start_button)
    bot.send_message(
        message.chat.id,
        "Приветствую тебя в нашей команде! Для начала тебе нужно выбрать категорию, в какой сфере деятельности ты хочешь начать работать.",
        reply_markup=markup,
    )


# Обработчик команды /start
@bot.message_handler(content_types=["new_chat_members"])
def send_welcome(message):
    # Создаем клавиатуру с одной кнопкой "Начать"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("Начать")
    markup.add(start_button)
    bot.send_message(
        message.chat.id,
        "Приветствую тебя в нашей команде! Для начала тебе нужно выбрать категорию, в какой сфере деятельности ты хочешь начать работать.",
        reply_markup=markup,
    )


# Обработчик нажатия на кнопку "Начать"
@bot.message_handler(func=lambda message: message.text == "Начать")
def show_specialties(message):
    # Создаем инлайн клавиатуру с выбором специальностей
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Добавляем кнопки
    buttons = [
        "Дизайн",
        "SMM-специалист",
        "Аналитик",
        "Веб-дизайн",
        "Копирайтинг",
        "3D графика",
        "Аутсорсинг",
        "Реклама и маркетинг",
        "Маркетплейс-менедж",
        "Другое",
    ]

    # Добавляем кнопки в клавиатуру
    for button in buttons:
        markup.add(types.KeyboardButton(button))

    bot.send_message(message.chat.id, "Выбери свою специальность:", reply_markup=markup)


bot.infinity_polling()
