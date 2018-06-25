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
import os
from tinydb import TinyDB, Query


db = None


def get_dbc():
    return db


def set_dbc(dbc):
    global db
    db = dbc


class DBC:
    def __init__(self, path=None):
        if path is None:
            self.db = TinyDB(os.path.join('my-config', 'chollos-db.json'))
        else:
            self.db = TinyDB(path)
        user_configuration = self.db.table('UserConfiguration')
        if len(self.db.table('UserConfiguration').all())==0:
            user_configuration.insert({'keywords': '*', 'merchants': '*'})

    def get_table(self, table_name):
        return self.db.table(table_name)

    def purge(self):
        self.db.purge_tables()
    
    def get_keywords(self):
        result = []
        if self.db.table('UserConfiguration').all()[0]['keywords']=='*':
            result.append(self.db.table('UserConfiguration').all()[0]['keywords'])
        else:
            result = self.db.table('UserConfiguration').all()[0]['keywords'].split(',')
        return result

    def get_merchants(self):
        result = []
        if self.db.table('UserConfiguration').all()[0]['merchants']=='*':
            result.append(self.db.table('UserConfiguration').all()[0]['merchants'])
        else:
            result = self.db.table('UserConfiguration').all()[0]['merchants'].split(',')
        return result

    def modify_keywords(self, keywords):
        user_configuration = self.db.table('UserConfiguration')
        query = Query()
        user_configuration.update({'keywords': keywords},
                             query.merchants == user_configuration.all()[0]['merchants'])

    def modify_merchants(self, merchants):
        user_configuration = self.db.table('UserConfiguration')
        query = Query()
        user_configuration.update({'merchants': merchants},
                             query.keywords == user_configuration.all()[0]['keywords'])