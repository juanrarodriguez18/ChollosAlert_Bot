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
import requests

def notify_new_chollo(bot, user_id, chollo):
    comercio = ''
    precio = ''
    cupon = ''
    link = chollo.link

    if chollo.comercio:
        comercio = '#'+chollo.comercio
        comercio = comercio.replace(' ','')
        comercio = comercio.replace('.','')
        comercio = comercio.replace('-','')

    if '€' in chollo.precio:
        precio = '💶 '+chollo.precio.replace('.',',')

    if chollo.cupon:
        cupon = '🔖 Cupón: '+chollo.cupon+'\n'

    if 'amazon' in chollo.comercio.lower():
        link = amazonLinks(chollo.link)

    chollo_string = '<b>'+chollo.titulo+'</b> '+comercio+'\n'+precio+'\n'+cupon+'\n'+chollo.descripcion+'\n\n 🔗 '+link+'\n\n'
    msg_send = bot.send_message(chat_id=user_id, parse_mode="html", text=chollo_string)
    return msg_send is not None

def amazonLinks(link):
    affiliate_suffix = '/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=juanrarodri05-21'
    affiliate_suffix_without_ref = '?ie=UTF8&psc=1&linkCode=ll1&tag=juanrarodri05-21'
    r = requests.get(link)
    if '?' in r:
        return r.split('?')[0]+affiliate_suffix_without_ref
    else:
        return r.url+affiliate_suffix
