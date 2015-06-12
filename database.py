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
        db = MySQLdb.connect(host=self.hostname,
            user=self.username,
            passwd=self.password,
            db=self.database)

        cur = db.cursor()
        return cur

    #pass table name here
    def showTables(self, table):
        cur = self.connect()
        cur.execute("SHOW TABLES")
































