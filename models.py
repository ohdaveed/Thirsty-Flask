import datetime

from peewee import *

from flask_login import UserMixin

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
    period = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now)
    last_watered = IntegerField()
    countdown_type = CharField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Countdown], safe=True)
    print("Created tables if they weren't already there")
    DATABASE.close()

