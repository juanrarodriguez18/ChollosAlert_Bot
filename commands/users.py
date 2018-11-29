# Copyright 2018 by ChollosAlert Bot contributors. All rights reserved.
#
# This file is part of ChollosAlert Bot.
#
#     ChollosAlert Bot is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     ChollosAlert Bot is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with ChollosAlert Bot.  If not, see <http:#www.gnu.org/licenses/>.

from telegram.ext import ConversationHandler
from repository.repository import DBC, get_dbc
import re

import logging

KEYWORDS = 1
MERCHANTS = 2
PRICE = 3

def list_keywords(bot, update):
    keywords = get_dbc().get_keywords_str(update.message.chat_id)

    update.message.reply_text("Su lista de Palabras Clave es:\n\n"+keywords)

def list_merchants(bot, update):
    merchants = get_dbc().get_merchants_str(update.message.chat_id)

    update.message.reply_text("Su lista de Comercios es:\n\n"+merchants)

def show_price(bot, update):
    price = get_dbc().get_price(update.message.chat_id)
    text = ''
    if price=='*':
        text = "Su precio máximo es:\n\n"+price
    else:
        text = "Su precio máximo es:\n\n"+price+" €"

    update.message.reply_text(text)

def modify_keywords(bot, update):
    keywords = get_dbc().get_keywords_str(update.message.chat_id)

    update.message.reply_text("""Introduzca una lista de Palabras Clave separadas por \",\" o escriba \"*\" si no desea configurar Palabras Clave.
    \nSu lista actual de Palabras clave es: \n"""+keywords)
    return KEYWORDS

def modify_user_keywords(bot, update):
    keywords = update.message.text
    get_dbc().modify_keywords(keywords, update.message.chat_id)

    update.message.reply_text("Se ha actualizado su lista de Palabras Clave.")

    return ConversationHandler.END

def modify_merchants(bot, update):
    merchants = get_dbc().get_merchants_str(update.message.chat_id)

    update.message.reply_text("""Introduzca una lista de Comercios separadas por \",\" o escriba \"*\" si no desea configurar Comercios.
    \nSu lista actual de Comercios es: \n"""+merchants)
    return MERCHANTS

def modify_user_merchants(bot, update):
    merchants = update.message.text
    get_dbc().modify_merchants(merchants, update.message.chat_id)

    update.message.reply_text("Se ha actualizado su lista de Comercios.")

    return ConversationHandler.END

def modify_price(bot, update):
    price = get_dbc().get_price(update.message.chat_id)
    text = ''

    if price=='*':
        text = """Introduzca un precio máximo, en caso de tener decimales, ha de incluirse con \",\" y no se ha de incluir el símbolo \"€\" o escriba \"*\" si no desea configurar Precio.
    \nSu Precio máximo actual es: \n"""+price
    else:
        text = """Introduzca un precio máximo, en caso de tener decimales, ha de incluirse con \",\" y no se ha de incluir el símbolo \"€\" o escriba \"*\" si no desea configurar Precio.
    \nSu Precio máximo actual es: \n"""+price+""" €"""

    update.message.reply_text(text)
    return PRICE

def modify_user_price(bot, update):
    price = update.message.text
    pattern = re.compile("^(\d*,)?\d+$")
    text = ''

    if pattern.match(price) or price=='*':
        get_dbc().modify_price(price, update.message.chat_id)
        text = "Se ha actualizado su Precio máximo."
    else:
        text = "No se ha introducido un precio válido."

    update.message.reply_text(text)

    return ConversationHandler.END

def cancel(bot, update):
    user = update.message.from_user
    logging.info("User %s canceled the conversation." % user.first_name)
    update.message.reply_text('Operación cancelada.')

    return ConversationHandler.END