import os

import datetime
from flask_login import UserMixin
from peewee import *

from playhouse.db_url import connect

if "ON_HEROKU" in os.environ:  # later we will manually add this env var
    # in heroku so we can write this code
    DATABASE = connect(os.environ.get("DATABASE_URL"))  # heroku will add this
    # env var for you
    # when you provision the
    # Heroku Postgres Add-on
else:

    DATABASE = SqliteDatabase("countdowns.sqlite")


class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE


class Countdown(Model):
    name = CharField()
    owner = ForeignKeyField(User, backref="countdowns")
    image = CharField()
    timer = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now)
    last_watered = IntegerField(default=0)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Countdown], safe=True)
    print("Created tables if they weren't already there")
    DATABASE.close()
