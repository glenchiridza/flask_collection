import datetime

# peewee is an Object Relational Mapper that turns your model objects into rows in your database
from peewee import *

DATABASE = SqliteDatabase('courses.sqlite')


class Course(Model):
    title = CharField()
    url = CharField(unique=True)
