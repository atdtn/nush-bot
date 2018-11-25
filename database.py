from mongoengine import *
from config import DATABASE_HOST, DATABASE_LOGIN, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_PORT

connect(DATABASE_NAME, host=DATABASE_HOST, port=DATABASE_PORT, username=DATABASE_LOGIN, password=DATABASE_PASSWORD)
print('Connected to {0}'.format(DATABASE_NAME))

LANGUAGES = ['ua']
ROLES = ['parent', 'teacher']


class User(Document):
    user_id = IntField(required=True)
    username = StringField()
    first_name = StringField()
    last_name = StringField()
    state = StringField()
    role = StringField(choices=ROLES, default=ROLES[0])
    language = StringField(choices=LANGUAGES, default=LANGUAGES[0])
