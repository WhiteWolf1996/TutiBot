import telebot
import config

bot = telebot.TeleBot('1194038676:AAGfrasBUmNx9Pj1ZyGyyf3wOaZETR9J6Kw')

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    
    bot.send_message(message.chat.id,"\t Salom 6e-17 buyuk talabasi {0.first_name} \n Sen ko'rib turgan bot buyuk programmist ДМИТРИЙ БЕЛЫЙ tomonidan yaratilgan .\n Ushbu bot hozircha faqat yozgan yozuvingni qaytaradi . \n (Shuming uchun nami YO'TI)".format(message.from_user,bot.get_me()),
        parse_mode='html')

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)
    
# RUN
bot.polling(none_stop=True)