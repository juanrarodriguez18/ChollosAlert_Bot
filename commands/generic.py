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
import time
from repository.repository import DBC, get_dbc
from services.cholloService import check_chollos_first_time
from config.loadConfig import Config, get_config


def start(bot, update):
    # print(update.message.chat_id)
    is_inserted = get_dbc().insert_user_configuration(update.message.chat_id)

    if is_inserted:
        update.message.reply_text("¡Se ha configurado el bot para ti ;)!")
        # Check if refresh time is larger than 3 seconds for send the chollos for the first time
        if(get_config().default_refresh_chollos > 3):
            time.sleep(3)
            check_chollos_first_time(update.message.chat_id)
    else:
        update.message.reply_text("¡Su usuario ya existe!")

def help(bot, update):
    update.message.reply_text("Éste Bot se ha desarrollado con la intención de no perderse los chollos que pueden resultar importantes sin tener que tener activas"+
    "las notificaciones de todos los canales de Chollos. Para ello se han definido dos listas:"+
    "\n\n\t - Lista de Palabras Clave: Permite al usuario elegir una lista de palabras claves para que se le notifiquen los chollos"+
    "que contengan sólo dichas palabras. En caso de querer ser notificados de todos los chollos, definiremos ésta lista como \"*\" (es como"+
    "viene definida por defecto)."+
    "\n\n\t - Lista de Comercios: Permite al usuario elegir una lista de comercios para que se le notifiquen los chollos"+
    "que contengan sólo dichos comercios. En caso de querer ser notificados de todos los chollos, definiremos ésta lista como \"*\" (es como"+
    "viene definida por defecto)."+
    "\n\n Si ambas listas están configuradas, el usuario sólo será notificado de aquellos chollos que cumplan las condiciones marcadas en"+
    "ambas listas. Los chollos se revisarán automáticamente cada "+str(get_config().default_refresh_chollos)+" segundos."+
    "\n\n Para cualquier duda, mejora o fallo en el Bot, sentíos libres de poner una Issue en el repositorio:"+ 
    "https://github.com/juanrarodriguez18/ChollosAlert_Bot")

def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))



