from datetime import datetime
from pymongo import MongoClient

from src.guardiannet.app.util import PasswordManager


class SystemInitializer:

    @staticmethod
    def initialize_system(username, password):
        client = None
        user = None

        try:
            client = MongoClient("localhost", 27017)
            db = client.guardian_net_db

            newUser = {
                "username": username,
                "password": PasswordManager.hashPassword(password),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            }

            users = db.users
            user = users.insert_one(newUser)
        except Exception as e:
            print(f"Caught an exception: {type(e).__name__}: {e}")
        finally:
            client.close()

        return True if user is not None else False
