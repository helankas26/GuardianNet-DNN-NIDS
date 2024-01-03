from mongoengine import connect
from pymongo import MongoClient


class MongoDBManager:
    db = "guardian_net_db"
    host = "localhost"
    port = 27017

    def __init__(self):
        connect(self.db, host=self.host, port=self.port)

    def closeConnection(self):
        pass

    @classmethod
    def doesDatabaseExists(cls):
        client = MongoClient(cls.host, cls.port)

        existing_databases = client.list_database_names()
        client.close()

        return cls.db in existing_databases
