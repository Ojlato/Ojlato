import telebot
from telebot import types
bot= telebot.TeleBot("7789371758:AAHxCthTSEzvSCBH92pyp8E-DsW8o34oi9Y")
fp=open("C:/Users/POURALI PC CENTER/Downloads/R (1).jpg",'rb')
sp=open("C:/Users/POURALI PC CENTER/Downloads/1da20f66-6c98-4079-8536-147c43d3b006.jpg",'rb')
#media=[]
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_chat_action(message.chat.id,action='upload_photo')
    #bot.send_photo(chat_id=message.chat.id,photo=fp,caption="متن اولیه")
    #bot.send_video(message.chat.id,open("D:/FFOutput/Shahrzad.S02E14.480p.Film2Movie_Asia 00_00_00-00_03_39.mp4",'rb'))
    #bot.send_document(message.chat.id,open("C:/Users/POURALI PC CENTER/OneDrive/Documents/khayati.pdf",'r'))
    #bot.send_audio(message.chat.id,open("C:/Users/POURALI PC CENTER/Downloads/Telegram Desktop/Shahin Najafi - ADHD (320).mp3",'rb'))
    #p1=types.InputMediaPhoto(open("C:/Users/POURALI PC CENTER/Downloads/1da20f66-6c98-4079-8536-147c43d3b006.jpg",'rb'))
    #p2=types.InputMediaPhoto(open("C:/Users/POURALI PC CENTER/Downloads/Top-programmer-wallpapers-768x407.jpg",'rb'))
    #p3=types.InputMediaPhoto(open("C:/Users/POURALI PC CENTER/Downloads/New folder/er.jpeg" , 'rb'))
    media.append(p1)
    media.append(p2)
    #media.append(p3)
    #bot.send_media_group(message.chat.id,media=media)

bot.polling(timeout=120)


def get(m):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    but=types.KeyboardButton(text='تلفن',request_contact=True)
    markup.add(but)
    bot.send_message(m.chat.id,"شماره خود را تایید کنید",reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def contact(m):
    print(m.contact)

bot.polling(timeout=120)

