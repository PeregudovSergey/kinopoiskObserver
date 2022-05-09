from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from requestHTML import *
import sys


def start(update, context): 	
	text = "I'm a bot, who helps you find a information about films!\n"
	text += "I have following commands\n"
	text += "/help\n"
	text += "/GetDescription [filmName]\n"
	
	f.write("call start:\n")		
	f.write(text + '\n')	
	f.flush()	
		

	context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def help(update, context): 	
	text = "I have following commands\n"
	text += "/start\n"
	text += "/GetDescription [filmName]\n"

	f.write("call help:\n") 
	f.write(text + '\n')
	f.flush()	

	context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def GetDescription(update, context):
	f.write("call GetDescription:\n") 
	f.write(' '.join(context.args) + '\n')
	f.flush()	

	info = getInfo(' '.join(context.args))
	description = getDescription(info)
	img = getPoster(info)
	context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)
	context.bot.send_message(chat_id=update.effective_chat.id, text=description)
	f.write("end GetDescription\n")
	f.flush()	

token = '5253461096:AAGf_sSTSe6L2nzCRKuZ9hn9qUWZTGhlwAU'
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)


getDescription_handler = CommandHandler('GetDescription', GetDescription)
dispatcher.add_handler(getDescription_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

updater.start_polling()
