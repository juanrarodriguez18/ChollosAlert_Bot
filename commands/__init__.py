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
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, \
    RegexHandler, Filters

from commands.generic import start, help, error
from commands.users import list_keywords, list_merchants, modify_keywords, modify_user_keywords, \
    modify_merchants, modify_user_merchants, cancel


def load_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    
    # LIST
    dispatcher.add_handler(CommandHandler('listarpalabrasclave', list_keywords))
    dispatcher.add_handler(CommandHandler('listarcomercios', list_merchants))

    # MODIFY KEYWORDS
    KEYWORDS = 1
    conv_modify_keywords = ConversationHandler(
        entry_points=[CommandHandler('modificarpalabrasclave', modify_keywords)],
        states={
            KEYWORDS: [MessageHandler(Filters.text, modify_user_keywords)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conv_modify_keywords)
    dispatcher.add_error_handler(error)

    # MODIFY MERCHANTS
    MERCHANTS = 2
    conv_modify_merchants = ConversationHandler(
        entry_points=[CommandHandler('modificarcomercios', modify_merchants)],
        states={
            MERCHANTS: [MessageHandler(Filters.text, modify_user_merchants)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conv_modify_merchants)
    dispatcher.add_error_handler(error)
