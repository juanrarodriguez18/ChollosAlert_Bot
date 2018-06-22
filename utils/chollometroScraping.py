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

# encoding:utf-8
import codecs
import sys
import requests
# from repository.chollo import Chollo

from bs4 import BeautifulSoup

def extraer_datos_pagina():
    url = 'https://www.chollometro.com/nuevos'
    headers = {'User-Agent':'Mozilla/5.0'}


    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    chollos = soup.find_all('article')

    titulo_chollo = ''
    comercio_chollo = ''
    precio_chollo = ''
    descripcion_chollo = ''
    cupon_chollo = ''
    link_chollo = ''
    result = []

    # Use "chcp 65001" command on windows console in order to show the string correctly
    for chollo in chollos:
        if chollo.find('strong', {"class": "thread-title"}) != None:
            titulo_chollo = chollo.find('strong', {"class": "thread-title"}).text.encode('utf-8').decode('utf-8').strip()
        if chollo.find('span', {"class": "cept-merchant-name"}) != None:
            comercio_chollo = chollo.find('span', {"class": "cept-merchant-name"}).text.encode('utf-8').decode('utf-8').strip()
        if chollo.find('span', {"class": "thread-price"}) != None:
            precio_chollo = chollo.find('span', {"class": "thread-price"}).text.encode('utf-8').decode('utf-8').strip()
        if chollo.find('div', {"class": "cept-description-container"}) != None:
            descripcion_chollo = chollo.find('div', {"class": "cept-description-container"}).text.encode('utf-8').decode('utf-8').strip()
        if chollo.find('div', {"class": "voucher"}) != None:
            cupon_chollo = chollo.find('div', {"class": "voucher"}).find('input').get('value').encode('utf-8').decode('utf-8').strip()
        if chollo.find('a', {"class": "btn--mode-primary"}) != None:
            link_chollo = chollo.find('a', {"class": "btn--mode-primary"}).get('href').encode('utf-8').decode('utf-8').strip()
        # cholloObject = Chollo(titulo_chollo, comercio_chollo, precio_chollo, descripcion_chollo, cupon_chollo, link_chollo)
        # result.append(cholloObject)
        print(titulo_chollo+' - '+comercio_chollo+' - '+precio_chollo+' - '+descripcion_chollo+' - '+cupon_chollo+' - '+link_chollo)
    
    return result


extraer_datos_pagina()