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

import logging
import schedule
import repository.repository as repository
from utils.chollometroScraping import extraer_datos_pagina_chollometro
from utils.micholloScraping import extraer_datos_pagina_michollo
from utils.telegram import notify_new_chollo
from services import get_bot


old_chollos = {}

def get_user_chollos(user_id):
    repository.set_dbc(repository.DBC())
    keywords = repository.get_dbc().get_keywords(user_id)
    merchants = repository.get_dbc().get_merchants(user_id)
    chollos = []
    chollos.extend(extraer_datos_pagina_chollometro() + extraer_datos_pagina_michollo())
    result = []

    # Use "chcp 65001" command on windows console in order to show the string correctly
    for chollo in chollos:
        for keyword in keywords:
            if ((keyword.strip() == '*' or keyword.strip().lower() in chollo.titulo.lower()) and 
                ('*'.strip() in merchants or chollo.comercio.strip().lower() in merchants.lower())):
                        # print(chollo.titulo+' - '+chollo.comercio+' - '+chollo.precio+' - '+chollo.descripcion+' - '+chollo.cupon+' - '+chollo.link)
                        result.append(chollo)
    
    return result

def check_chollos():
        logging.debug("Checking chollos")
        result = []
        try:
            for userConfiguration in repository.get_dbc().get_table('UserConfiguration').all():
                user_id = userConfiguration['user_id']
                chollos = get_user_chollos(user_id)
                if user_id not in old_chollos:
                    old_chollos[user_id] = []
                for chollo in chollos:
                    if chollo.link not in old_chollos[user_id]:
                        result.append(chollo)
                        old_chollos[user_id].append(chollo.link)
                        notify_new_chollo(get_bot(), user_id, chollo)
                        # print(chollo.titulo+' - '+chollo.comercio)
        except Exception as e:
            logging.error("Failed checking chollos")
            logging.error(e)
            # get_bot().send_message(chat_id=user_id, parse_mode="Markdown", text="Something go really bad. You couldn't be notify of news chollos")
        return result

def check_chollos_first_time(user_id):
        logging.debug("Checking chollos")
        result = []
        try:
            user_id = user_id
            chollos = get_user_chollos(user_id)
            if user_id not in old_chollos:
                old_chollos[user_id] = []
            for chollo in chollos:
                if chollo.link not in old_chollos[user_id]:
                    result.append(chollo)
                    old_chollos[user_id].append(chollo.link)
                    notify_new_chollo(get_bot(), user_id, chollo)
                    # print(chollo.titulo+' - '+chollo.comercio)
        except Exception as e:
            logging.error("Failed checking chollos")
            logging.error(e)
            # get_bot().send_message(chat_id=user_id, parse_mode="Markdown", text="Something go really bad. You couldn't be notify of news chollos")
        return result

def schedule_chollos(time_seconds):
    # print(time_seconds)
    schedule.every(time_seconds).seconds.do(check_chollos)
    