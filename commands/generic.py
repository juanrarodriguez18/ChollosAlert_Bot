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
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
from repository.repository import DBC, get_dbc


def start(bot, update):
    # print(update.message.chat_id)
    is_inserted = get_dbc().insert_user_configuration(update.message.chat_id)

    if is_inserted:
        update.message.reply_text("¡Se ha configurado el bot para ti ;)!")
    else:
        update.message.reply_text("¡Su usuario ya existe!")

def help(bot, update):
    update.message.reply_text("help")


def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))



