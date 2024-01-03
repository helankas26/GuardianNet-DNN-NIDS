from datetime import datetime
from mongoengine import Document, StringField, DateTimeField


class Users(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M"))
