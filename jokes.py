import telebot
import constants
import json

bot = telebot.TeleBot(constants.token)

players = {}

print (bot.get_me())
@bot.message_handler(content_types=['new_chat_member'])
def newPlayer(message):
    chatId=str(message.chat.id)
    userId = str(message.from_user.id)
    if userId == '@painstyle01':
        bot.send_message(int(chatId), str ("Создателя разбанили!"))

    if userId == '@Raneddo':
        bot.send_message(int(chatId), str("Создателя разбанили!"))

    if userId == '@su4ara':
        bot.send_message(int(chatId), str("Шпион! На кол!"))

