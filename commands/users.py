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

import logging

KEYWORDS = 1
MERCHANTS = 2

def list_keywords(bot, update):
    keywords = get_dbc().get_keywords_str(update.message.chat_id)

    update.message.reply_text("Su lista de Palabras Clave es:\n\n"+keywords)

def list_merchants(bot, update):
    merchants = get_dbc().get_merchants_str(update.message.chat_id)

    update.message.reply_text("Su lista de Comercios es:\n\n"+merchants)

def modify_keywords(bot, update):
    keywords = get_dbc().get_keywords_str(update.message.chat_id)

    update.message.reply_text("""Introduzca una lista de Palabras Clave separadas por \",\" o escriba \"*\" si no desea configurar Palabras Clave.
                             \n\nSu lista actual de Palabras clave es: """+keywords)
    return KEYWORDS

def modify_user_keywords(bot, update):
    keywords = update.message.text
    get_dbc().modify_keywords(keywords, update.message.chat_id)

    update.message.reply_text("Se ha actualizado su lista de Palabras Clave.")

    return ConversationHandler.END

def modify_merchants(bot, update):
    merchants = get_dbc().get_merchants_str(update.message.chat_id)

    update.message.reply_text("""Introduzca una lista de Comercios separadas por \",\" o escriba \"*\" si no desea configurar Comercios.
                             \n\nSu lista actual de Comercios es: """+merchants)
    return MERCHANTS

def modify_user_merchants(bot, update):
    merchants = update.message.text
    get_dbc().modify_merchants(merchants, update.message.chat_id)

    update.message.reply_text("Se ha actualizado su lista de Comercios.")

    return ConversationHandler.END

def cancel(bot, update):
    user = update.message.from_user
    logging.info("User %s canceled the conversation." % user.first_name)
    update.message.reply_text('Operación cancelada.')

    return ConversationHandler.END