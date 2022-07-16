import datetime
from argon2 import PasswordHasher
# peewee is an Object Relational Mapper that turns your model objects into rows in your database
from peewee import *

DATABASE = SqliteDatabase('courses.sqlite')


class Course(Model):
    title = CharField()
    url = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


class Review(Model):
    course = ForeignKeyField(Course, related_name='review_set')
    rating = IntegerField()
    comment = TextField(default='')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Course, Review], safe=True) # safe=True is so that it jus passes if those tables already
    # exist in DB instead of error
    DATABASE.close()


