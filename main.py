
__version__ = 0.9
import telebot
import constants
import json

bot = telebot.TeleBot(constants.token)

players = {}
"""
print (bot.get_me())

bot.send_message(-1001045426965, "Я обновился. Почистил логи. Готов к работе")
bot.send_message(-1001045426965, "Писатель Гудвин был творцом строки со стажем. ")
bot.send_message(-1001045426965, "К несчастью, все его друзья перевелись.")
bot.send_message(-1001045426965, "Но лишь я стал его любимым персонажем,")
bot.send_message(-1001045426965, "Как у меня проблемы в жизни начались.")

upd = bot.get_updates()
last_upd = upd [-1]
message_from_user =last_upd.message
print(message_from_user)
"""
# Пуллеры

@bot.message_handler(content_types=["command"])
def handle_command(message):
    print ("Прислали команду")

@bot.message_handler(content_types=["text"])
def handle_command(message):
    print ("Прислали текст")

@bot.message_handler(content_types=["document"])
def handle_command(message):
    print ("Прислали док")

@bot.message_handler(content_types=["audio"])
def handle_command(message):
    print ("Прислали звук")

@bot.message_handler(content_types=["photo"])
def handle_command(message):
    print("Прислали фото")

@bot.message_handler(content_types=["sticker"])
def handle_command(message):
    print ("Прислали наклейку")

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, 'Мне плохо')


@bot.message_handler(content_types=['new_chat_member'])
def newPlayer(message):
    chatId = str(message.chat.id)
    userId = str(message.from_user.id)
    # print(username)
    if chatId not in players:
        players[chatId] = []

    if userId not in players[chatId]:
        players[chatId].append(str(userId))

    username = '@' + str(message.from_user.username)
    print (username)

    if username == '@None':
        username = message.from_user.first_name

    bot.send_message(-1001140294198, str("Привет, " + \
                                      str(username) + ". Добро пожаловать в Мятный Замок! Наш замковый бот: @MintFortressBot \n"
                                      "Наши отряды: https://t.me/MintNews/78 \n"
                                      "Наша газета : @MintNews \n"
                                      "Чат для трейда : @minttrade \n"
                                      "Правила мятного замка: http://telegra.ph/Pravila-Myatnogo-chata-05-03  \n"
                                      "Флуд-чаты мятного замка: http://telegra.ph/Mint-Flood-Chats-List-05-10  \n"
                                      "Наше радио @MintFM  \n"
                                      "Мятная мафия: https://t.me/joinchat/AAAAAEG4lufeLiEzQ6swsg"), disable_web_page_preview=True)

    writefile = open('list.py', 'w')
    f = json.dumps(players)
    writefile.write(str(f))
    writefile.close()


# Ливнул

try:
    readfile = open('list.py')
    players = json.load(readfile)
    bot.polling(none_stop=True, interval=0)
    readfile.close()
except:
    writefile = open('list.py', 'w')
    f = json.dumps(players)
    writefile.write(str(f))
    writefile.close()
