import telebot
import constants
from telebot import types

bot = telebot.TeleBot(constants.token)
markup = types.ReplyKeyboardMarkup(True)
markup.row('/request')
markup.row('/feedback')
markup2 = types.ReplyKeyboardMarkup(True)
markup2.row('/restart')

@bot.message_handler(commands=['start'])
def keyboard(message):
    chatId = message.chat.id
    if chatId == -1001124048974:
        bot.send_message(chatId,'Вам делать нечего? ЗА РАБОТУ!')
    bot.send_message(chatId, 'Привет. Выбери что ты хочешь сделать из пункта ниже:',  reply_markup=markup)



@bot.message_handler(commands=['request'])
def request(message):
    chatId = message.chat.id
    if chatId == -1001124048974:
        bot.send_message(chatId,'Вам делать нечего? ЗА РАБОТУ!')
    bot.send_message(chatId, 'Есть интересная новость? Расскажи её нам! (/send "Текст новости".'
                             'Если хочешь вернуться в меню нажми "/restart"', reply_markup=markup2)

@bot.message_handler(commands=['feedback'])
def request(message):
    chatId = message.chat.id
    if chatId == -1001124048974:
        bot.send_message(chatId,'Вам делать нечего? ЗА РАБОТУ!')
    bot.send_message(chatId, 'Жалоба, предложение или идея? Отправь её нам! (/send "Текст обращения").'
                             'Если хочешь вернуться в меню нажми "/restart"', reply_markup=markup2)


@bot.message_handler(commands=['restart'])
def restart(message):
    chatId = message.chat.id
    if chatId == -1001124048974:
        bot.send_message(chatId,'Вам делать нечего? ЗА РАБОТУ!')
    bot.send_message(chatId, 'Отменено.')
    bot.send_message(chatId, 'Привет. Тут ты можешь оставить свой отзыв', reply_markup=markup)

@bot.message_handler(commands=['ping'])
def ping(message):
    chatId = message.chat.id
    bot.send_message(chatId, 'Да работаю я бл***')

@bot.message_handler(commands=['send'])
def send(message):
    username = '@' + str(message.from_user.username)
    if username == '@None':
        username = message.from_user.first_name
    chatId = message.chat.id
    text = message.text
    bot.send_message(chatId, 'Ты отправил в редакцию слова: ' + str(text))
    bot.send_message(chatId, 'Отправлено! Что то ещё?', reply_markup=markup)
    bot.send_message(-1001124048974,'Господа, к нам обращение от ' + str(username))
    bot.send_message(-1001124048974, str(text))
    
if __name__ == '__main__':
     bot.polling(none_stop=True)
