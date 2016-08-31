# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("197711945:AAHgjrTGp7CSLqi7YTBbfCHAtcsNGphNh4s")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)