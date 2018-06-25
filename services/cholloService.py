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

import repository.repository as repository
from utils.chollometroScraping import extraer_datos_pagina_chollometro
from utils.micholloScraping import extraer_datos_pagina_michollo

def get_user_chollos():
    repository.set_dbc(repository.DBC())
    keywords = repository.get_dbc().get_keywords()
    merchants = repository.get_dbc().get_merchants()
    chollos = []
    chollos.extend(extraer_datos_pagina_chollometro() + extraer_datos_pagina_michollo())
    result = []

    for chollo in chollos:
        for keyword in keywords:
            if (keyword == '*' or keyword in chollo.titulo) and ('*' in merchants or chollo.comercio in merchants):
                        print(chollo.titulo+' - '+chollo.comercio+' - '+chollo.precio+' - '+chollo.descripcion+' - '+chollo.cupon+' - '+chollo.link)
                        result.append(chollo)
    
    return result
    