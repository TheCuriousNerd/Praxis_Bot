# The main repository of Praxis Bot can be found at: <https://github.com/TheCuriousNerd/Praxis-Bot>.
# Copyright (C) 2021

# Author Info Examples:
#   Name / Email / Website
#       Twitter / Twitch / Youtube / Github

# Authors:
#   Alex Orid / inquiries@thecuriousnerd.com / TheCuriousNerd.com
#       Twitter: @TheCuriousNerd / Twitch: TheCuriousNerd / Youtube: thecuriousnerd / Github: TheCuriousNerd

# This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sqlalchemy as db

import credentials
import config
class Praxis_DB_Connection():
    def __init__(self, autoConnect:bool=False):
        super().__init__()
        self.credentials_manager = credentials.Credentials_Module()
        self.credentials_manager.load_credentials()
        self.dbCert: credentials.DB_Credential = self.credentials_manager.find_Credential(credentials.DB_Credential, config.credentialsNickname)

        self.connectionString = "postgresql://%s:%s@%s/%s" % (self.dbCert.username, self.dbCert.password, self.dbCert.ipAddress, self.dbCert.databaseName)

        self.dbConnection = None
        if autoConnect == True:
            self.startConnection()

    def startConnection(self):
        self.dbConnection = db.create_engine(self.connectionString)

    def closeConnection(self):
        self.dbConnection = None

    def execQuery(self, query):
        try:
            return self.dbConnection.execute(query)
        except:
            print("[Praxis_DB_Connection] query error")
            return None