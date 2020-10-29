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
import requests
from repository.chollo import Chollo

from bs4 import BeautifulSoup


def extraer_datos_pagina_michollo():
    url = 'https://michollo.com'
    headers = {'User-Agent': 'Mozilla/5.0'}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    chollos = soup.find_all('article', {"class": "offer_grid_com"})

    result = []

    # Use "chcp 65001" command on windows console in order to show the string correctly
    for chollo in chollos:
        titulo_chollo = ''
        comercio_chollo = ''
        precio_chollo = ''
        descripcion_chollo = ''
        cupon_chollo = ''
        link_chollo = ''

        if chollo.find('h3') != None:
            titulo_chollo = chollo.find('h3').find('a').text.encode('utf-8').decode('utf-8').strip()
        if chollo.find('div', {"class": "cat_store_for_grid"}) != None:
            comercio_chollo = chollo.find('div', {"class": "cat_store_for_grid"}).text.encode('utf-8').decode('utf-8').strip()
        if chollo.find('span', {"class": "rh_regular_price"}) != None:
            precio_chollo = chollo.find('span', {"class": "rh_regular_price"}).text.encode('utf-8').decode('utf-8').strip().split()[0]
        if chollo.find('div', {"class": "grid_row_info"}) != None:
            descripcion_chollo = chollo.find('div', {"class": "grid_row_info"}).find('h3').find('a').text.encode('utf-8').decode('utf-8').strip()
        if chollo.find('span', {"class": "coupon_text"}) != None:
            cupon_chollo = chollo.find('span', {"class": "coupon_text"}).text.encode('utf-8').decode('utf-8').strip()
        if chollo.find('div', {"class": "btn_offer_block"}) != None:
            link_chollo = chollo.find('div', {"class": "btn_offer_block"}).get('url').encode('utf-8').decode('utf-8').strip()

        #print("Titulo: "+titulo_chollo+" | Comercio: "+comercio_chollo+" | Precio: "+precio_chollo+" | Descripcion: "+
        #         descripcion_chollo+" | Cupon: "+cupon_chollo+" | Link: "+link_chollo)
        chollo_object = Chollo(titulo_chollo, comercio_chollo, precio_chollo, descripcion_chollo, cupon_chollo, link_chollo)
        result.append(chollo_object)
    
    return result


# extraer_datos_pagina_michollo()
