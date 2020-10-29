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
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options  
import time

def extraer_datos_pagina_chollometro():
    url = 'https://www.chollometro.com/nuevos'

    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-setuid-sandbox')
    driver = webdriver.Chrome(chrome_options=options) #webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver.get(url)

    ScrollNumber = 500
    for i in range(1,ScrollNumber):
        driver.execute_script("window.scrollTo(1,10000)")
        # time.sleep(5)

    
    soup = BeautifulSoup(driver.page_source,'html.parser')
    chollos = soup.find_all('article')

    result = []

    # Use "chcp 65001" command on windows console in order to show the string correctly
    for chollo in chollos:
        titulo_chollo = ''
        comercio_chollo = ''
        precio_chollo = ''
        descripcion_chollo = ''
        cupon_chollo = ''
        link_chollo = ''

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

        #print("Titulo: "+titulo_chollo+" | Comercio: "+comercio_chollo+" | Precio: "+precio_chollo+" | Descripcion: "+
        #         descripcion_chollo+" | Cupon: "+cupon_chollo+" | Link: "+link_chollo)
        chollo_object = Chollo(titulo_chollo, comercio_chollo, precio_chollo, descripcion_chollo, cupon_chollo, link_chollo)
        result.append(chollo_object)
    
    

    return result


# extraer_datos_pagina_chollometro()
