import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
token='6536802362:AAGCoGs1jF7tcuBkrCz_ZvRtLjEwXSMjjuA'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Купить ⚡️Plus", url="https://www.youtube.com/watch?v=4qHaXH2ovS0"))
    return markup


@bot.message_handler(commands=['pay'])
def message_handler(message):
    bot.send_message(message.chat.id, "Подписка ⚡️Plus:\n" 
"- GEMINI-1.0 — безлимитно;\n"
"- GEMINI-1.5 — 50 запросов в день;\n" 
" Стоимость: 499.00р / за 30д ", reply_markup=gen_markup())


@bot.message_handler(commands=['who'])
def start_message(message):
  bot.send_message(message.chat.id,"Как я могу помочь в написании кода: \n"
"👨‍💻1. Автоматизация рутинных задач:\n"
"Я могу генерировать повторяющиеся фрагменты кода, такие как циклы for и while.\n"
"Я могу автоматически форматировать код, делая его более читаемым.\n"
"Я могу помочь вам с отладкой кода, указывая на возможные ошибки.\n"
"💡2. Генерация идей:\n"
"Я могу помочь вам сгенерировать новые идеи для ваших программ.\n"
"Я могу предложить вам разные способы реализации ваших идей.\n"
"Я могу помочь вам выбрать наиболее подходящий инструмент для вашей задачи.\n"
"🔎3. Поиск информации:\n"
"Я могу помочь вам найти информацию о языках программирования, библиотеках и фреймворках.\n"
"Я могу найти для вас примеры кода и учебные пособия.\n"
"Я могу ответить на ваши вопросы о языках программирования и кодировании.\n"
"🗣️4. Общение:\n"
"Я могу помочь вам общаться с другими разработчиками, объясняя им ваш код и идеи.\n"
"Я могу переводить код с одного языка программирования на другой.\n"
"Я могу помочь вам написать документацию к вашему коду.\n"
"🎨5. Творчество:\n"
"Я могу помочь вам создать новые и интересные программы.\n"
"Я могу помочь вам сделать ваш код более читаемым и красивым.\n"
"Я могу помочь вам выразить свою креативность через код.\n"
"Я постоянно учусь и совершенствуюсь, поэтому мои возможности в области кодирования будут только расширяться.\n"
"Я лучше chat-gpt \n"
"Пожалуйста, дайте мне знать, как я могу помочь вам в написании кода.")

bot.infinity_polling()










#token='6536802362:AAGCoGs1jF7tcuBkrCz_ZvRtLjEwXSMjjuA'