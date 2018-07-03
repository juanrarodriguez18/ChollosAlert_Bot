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
from repository.repository import DBC

import logging

KEYWORDS = 1
MERCHANTS = 2

def modify_keywords():
    None

def modify_user_keywords():
    None

def modify_merchants():
    None

def modify_user_merchants():
    None

def cancel(bot, update):
    user = update.message.from_user
    logging.info("User %s canceled the conversation." % user.first_name)
    update.message.reply_text('Operation cancelled, you have stopped the Account process.')

    return ConversationHandler.END