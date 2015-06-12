__author__ = 'nemanemati'

import MySQLdb

class myDb(object):

    def __init__(self, hostname, username, password, database):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database

    def getHostname(self):
        return self.hostname

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getDatabase(self):
        return self.database

    def connect(self):
        db = MySQLdb.connect(host=self.hostname, # your host, usually localhost
            user=self.username, # your username
            passwd=self.password, # your password
            db=self.database) # name of the data base

        return db

    def showTables(self):
        





















