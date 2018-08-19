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
from tinydb import TinyDB, Query, where
from tinydb.operations import add


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
        self.db.table('UserConfiguration')
        self.db.table('UserSentChollos')

    def get_table(self, table_name):
        return self.db.table(table_name)

    def purge(self):
        self.db.purge_tables()

    def insert_user_configuration(self, user_id):
            result = False
            if len(self.db.table('UserConfiguration').search(where('user_id') == user_id)) == 0:
                self.db.table('UserConfiguration').insert({'user_id': user_id, 'keywords': '*', 'merchants': '*'})
                result = True

            return result
    
    def get_keywords(self, user_id):
        result = []
        keywords = self.db.table('UserConfiguration').search(where('user_id') == user_id)[0]['keywords']
        if keywords=='*' or ',' not in keywords:
            result.append(keywords)
        else:
            result = keywords.split(',')
        return result

    def get_merchants(self, user_id):
        result = []
        merchants = self.db.table('UserConfiguration').search(where('user_id') == user_id)[0]['merchants']
        if merchants=='*' or ',' not in merchants:
            result.append(merchants)
        else:
            result = merchants.split(',')
        return result

    def modify_keywords(self, keywords, user_id):
        user_configuration = self.db.table('UserConfiguration')
        query = Query()
        user_configuration.update({'keywords': keywords.replace('"','')},
                             query.user_id == user_id)

    def modify_merchants(self, merchants, user_id):
        user_configuration = self.db.table('UserConfiguration')
        query = Query()
        user_configuration.update({'merchants': merchants.replace('"','')},
                             query.user_id == user_id)

    def get_keywords_str(self, user_id):
        return self.db.table('UserConfiguration').search(where('user_id') == user_id)[0]['keywords']

    def get_merchants_str(self, user_id):
        return self.db.table('UserConfiguration').search(where('user_id') == user_id)[0]['merchants']

    def insert_user_sent_chollos(self, user_id):
            result = False
            if len(self.db.table('UserSentChollos').search(where('user_id') == user_id)) == 0:
                self.db.table('UserSentChollos').insert({'user_id': user_id, 'chollos': []})
                result = True

            return result

    def get_user_sent_chollos(self, user_id):
        return self.db.table('UserSentChollos').search(where('user_id') == user_id)[0]['chollos']

    def add_user_sent_chollo(self, chollo, user_id):
        user_configuration = self.db.table('UserSentChollos')
        query = Query()
        user_configuration.update(add('chollos',[chollo]),
                             query.user_id == user_id)