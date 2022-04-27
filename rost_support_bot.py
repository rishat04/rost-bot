#from urllib import response
import telebot
from telebot import types
#import requests, json

old_token = "5308846060:AAE4ishCZ3H0Z0K8DgJ9ZIRKGgCGIZnDVBs"
TOKEN = "5326541238:AAHMUfujb90u3i8lWzWe7gVUn5sa4tZIAvc"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

chat_id = 1058605380

@bot.message_handler(commands=['start'])
def start_work(msg):
    print(msg.chat.username)
    bot.send_message(msg.chat.id, "Hello, @" + msg.chat.username)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Создать заявку')
    btn2 = types.KeyboardButton('Мои заявки')
    btn3 = types.KeyboardButton('Как пользоваться')
    markup.add(btn1, btn2, btn3)
    bot.send_message(msg.chat.id, "Начнем работать?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_requests(msg):
    if msg.text == 'Мои заявки':
        """response = requests.get("http://127.0.0.1:8000/heroes")
        for req in json.loads(response.text):
            #print(req)
            message = ''
            message += 'id:' + str(req['id']) + '\n'
            message += 'name: ' + req['name'] + '\n'
            message += 'alias: ' + req['alias'] + '\n'
            message += '_______________'
            bot.send_message(msg.chat.id, message)"""
        bot.send_message(msg.chat.id, msg.text)

    if msg.text == 'Как пользоваться':
        bot.send_message(msg.chat.id, msg.text)
    if msg.text == 'Создать заявку':
        #bot.send_message(msg.chat.id, 'Создаем заявку')
        #bot.send_message(msg.chat.id, 'Введите имя:')
        #name = msg.text
        
        ##bot.send_message(msg.chat.id, 'Введите ТЕКСТ:')
        #alias = msg.text
        #print(name , alias)
        #data = {'name': '', 'alias': ''}
        #res = requests.post('http://127.0.0.1:8000/api', data=data)
        ##print(res.text)
        bot.send_message(msg.chat.id, msg.text)




bot.infinity_polling()
