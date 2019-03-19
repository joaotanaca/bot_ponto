#!/usr/bin/env python3

import logging
from time import strftime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ChatAction
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from functools import wraps
from openpyxl import Workbook
from datetime import datetime
from datetime import date
import csv
import os.path

book=Workbook()
sheet=book.active
file_csv=open('folhaPonto.csv')
pasta_primaria='/home/PF/joao.jptr/Projetos/relogio-ponto/Planilhas'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def send_typing_action(func):
  @wraps(func)
  def command_func(*args, **kwargs):
    bot, update = args
    bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
    return func(bot, update, **kwargs)

  return command_func

@send_typing_action
def ponto(bot, update):
  keyboard = [[InlineKeyboardButton("Entrada", callback_data='1')],
                 [InlineKeyboardButton("Saida", callback_data='2')],
                [InlineKeyboardButton("Salvar folha de ponto", callback_data='3')]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  update.message.reply_text('Opa! Deseja registrar a entrada ou a saida?:', reply_markup=reply_markup)

@send_typing_action










def button(bot, update):
  
  query = update.callback_query
  opt=str(query.data)
  chat_id=query.message.chat_id
  now=datetime.now()
  date_mes=date.today().month
  dia_ponto=date.today().day
  pasta_user='{pasta}/{id}'.format(pasta=pasta_primaria, id=chat_id)
  pasta_planilha_mes='{pasta_user}/{mes}'.format(pasta_user=pasta_user, mes=date_mes)
  enviar_chat='{}/folhaPonto.csv'.format(pasta_planilha_mes)

  if os.path.isdir(pasta_planilha_mes):
    pass
  else:
    os.mkdir(pasta_planilha_mes)
    pass

  try:
    f=open(enviar_chat, 'w+')
    writer=csv.writer(f)
    writer.writerow( ('Dia','Entrada','Saida') )
  finally:
    pass

  if os.path.isdir(pasta_user):
    pass
  else:
    os.mkdir(pasta_user)

  if opt == '1':
    entrada='{}:{}'.format(now.hour, now.minute)
    bot.edit_message_text(text="Entrada registrada",chat_id=chat_id,message_id=query.message.message_id)
  elif opt=='2':
    saida='{}:{}'.format(now.hour, now.minute)
    bot.edit_message_text(text="Saida registrada",chat_id=chat_id,message_id=query.message.message_id)
  elif opt=='3': 
    try:
      f=open(enviar_chat, 'a')
      writer=csv.writer(f)
      ponto='{}'.format(date.today()), '{}'.format(entrada), '{}'.format(saida)
      writer.writerow((ponto))
      bot.edit_message_text(text="Folha do ponto do mês salva",chat_id=query.message.chat_id,message_id=query.message.message_id)
      bot.send_document(chat_id=chat_id,document=open(enviar_chat, 'rb'))
    finally:
      f.close()
@send_typing_action











def tecladoreplay(bot, update):
  location_keyboard = KeyboardButton(text="send_location", request_location=True)
  contact_keyboard = KeyboardButton(text="send_contact", request_contact=True)
  custom_keyboard = [[ location_keyboard, contact_keyboard ]]
  reply_markup = ReplyKeyboardMarkup(custom_keyboard)
  bot.send_message(chat_id=update.message.chat_id,
    text="Você se importaria em compartilhar sua 📍 localização e entrar em contato comigo?",
    reply_markup=reply_markup)

@send_typing_action
def horas(bot, update):
  msg = "Olá {user_name} agora são: ⏱ "
  msg += strftime('%H:%M:%S')
  bot.send_message(chat_id=update.message.chat_id,
    text=msg.format(user_name=update.message.from_user.first_name),
    parse_mode=ParseMode.MARKDOWN)

def error(bot, update, error):
  logger.warning('Update "%s" caused error "%s"', update, error)

def main():
  up = Updater('715491898:AAEBhodRvnVokRmu3LvovVbZTsE3AZxRkFU')

  up.dispatcher.add_handler(CommandHandler('horas', horas))
  up.dispatcher.add_handler(CommandHandler('ponto', ponto))
  up.dispatcher.add_handler(CallbackQueryHandler(button))
  up.dispatcher.add_handler(CommandHandler('replay', tecladoreplay))
  up.dispatcher.add_error_handler(error)
#  up.idle()

  up.start_polling()

if __name__ == '__main__':
  main()

# -*- coding:utf-8 -*-
# vim: set expandtab:noai:ts=2:sw=2
