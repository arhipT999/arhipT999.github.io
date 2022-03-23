from ast import Global
from cgitb import text
import sys
import telebot
from telebot import types
import os
import time

bot = telebot.TeleBot('5238341860:AAH6SZn1I4mYcFbopzJqJnteu5AI21jF-Q4')

@bot.message_handler(commands="reset", func= lambda message: message.from_user.id == 5131695189) 
def message(message):
    bot.send_message(message.from_user.id, 'Перезагрузка...')
    python = sys.executable
    os.execl(python, python, * sys.argv)


@bot.message_handler(commands="end", func= lambda message: message.from_user.id == 5131695189) 
def message(message):
    bot.send_message(message.from_user.id, 'Выключение...')
    bot.stop_polling()
    quit()


@bot.message_handler(commands="start")
def message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.username}! я Arhip_Tbot введи команду "/next" чтобы продолжить')
    with open('chatids.txt', 'a+') as chatids:
        if message.chat.id in chatids:
            pass
        else:
            print(message.chat.id, file=chatids)
@bot.message_handler(commands=['rassylka'])
def rassylka(message):
    if message.chat.id == '5131695189':
        for i in open('chatids.txt', 'r').readlines():
            bot.send_message(i, 'Рассылка')

@bot.message_handler(func = lambda m: True if 'бот' in m.text.lower() else False)
def secret(message):
    bot.send_message(message.chat.id, 'А я админу расказал... И ещё держи мут :)')
    bot.send_message(5131695189, f'Сообщение от: {message.from_user.username}, текст: {message.text}!')

@bot.message_handler(func = lambda m: True if 'лох' in m.text.lower() else False)
def secret(message):
    bot.send_message(message.chat.id, 'А я админу расказал... И ещё держи мут :)')
    bot.send_message(5131695189, f'Сообщение от: {message.from_user.username}, текст: {message.text}!')

@bot.message_handler(func = lambda m: True if 'дебил' in m.text.lower() else False)
def secret(message):
    bot.send_message(message.chat.id, 'А я админу расказал... И ещё держи мут :)')
    bot.send_message(5131695189, f'Сообщение от: {message.from_user.username}, текст: {message.text}!')

@bot.message_handler(func = lambda m: True if 'имбицил' in m.text.lower() else False)
def secret(message):
    bot.send_message(message.chat.id, 'А я админу расказал... И ещё держи мут :)')
    bot.send_message(5131695189, f'Сообщение от: {message.from_user.username}, текст: {message.text}!')

@bot.message_handler(func = lambda m: True if 'тупой' in m.text.lower() else False)
def secret(message):
    bot.send_message(message.chat.id, 'А я админу расказал... И ещё держи мут :)')
    bot.send_message(5131695189, f'Сообщение от: {message.from_user.username}, текст: {message.text}!')

@bot.message_handler(commands=['next'])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtna = types.KeyboardButton('/news')
    itembtnv = types.KeyboardButton('/start')
    itembtnz = types.KeyboardButton('/otziv')
    itembtnq = types.KeyboardButton('/random')
    markup.add(itembtna, itembtnv, itembtnz, itembtnq)
    bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)

@bot.message_handler(commands=['random'])
def random(message):
    sent = bot.send_dice(message.chat.id, '🎲')
    time.sleep(3.56)
    bot.send_message(message.chat.id, f'Поздравляю! Тебе выпало число {sent.dice.value}')

@bot.message_handler(commands=['news'])
def news(message):
    import requests 
    from bs4 import BeautifulSoup
    url = 'https://lenta.ru/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    link = 'https://lenta.ru/'+soup.find('div', class_='last24').find('a', class_='card-mini _compact').get('href')
    bot.send_message(message.chat.id, link)


@bot.message_handler(commands=['otziv'])
def otziv(message):
    sent = bot.reply_to(message, 'Пожалуйста, оставьте отзыв!')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    message_to_save = message.text
    bot.send_message(-675584103, f'Отзыв от {message.from_user.username}:{message_to_save}')
    bot.send_message(5131695189, f'Отзыв от {message.from_user.username}:{message_to_save}')
    bot.send_message(message.from_user.id, 'Спасибо!')

@bot.edited_message_handler(func=lambda message: True)
def edit(message: types.Message):
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.id+1, text=f"Сам {message.text}!")


@bot.message_handler(func=lambda message:True)
def otvet(message):
    bot.send_message(message.chat.id, f'"{message.text}" и зачем ты это пишешь?')
bot.polling()