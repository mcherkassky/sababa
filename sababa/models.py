from mongoengine import *
from flask_login import UserMixin
import json

from bs4 import *
from bson import json_util, ObjectId, DBRef
from mongoengine.dereference import DeReference

from settings import *
# from url import *

from datetime import datetime
from json import JSONEncoder

def mongoencode(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, DBRef):
        obj_db = DeReference()({'data': obj})['data']
        return obj_db._data
    else:
        return obj._data

class CustomQuerySet(QuerySet):
    # def to_json(self, *args, **kwargs):
    #     import pdb; pdb.set_trace()
    #     return json_util.dumps([serialize(obj) for obj in self.as_pymongo()], *args, **kwargs)
    def json(self):
        return '[' + ','.join([obj.json() for obj in self]) + ']'

class Base(object):
    meta = {'allow_inheritance': True,
            'queryset_class': CustomQuerySet}

    # def serialize(self, *args, **kwargs):
    #     import pdb; pdb.set_trace()
        # return json_util.dumps(serialize(self.to_mongo()),  *args, **kwargs)

    def json(self):
        return json.dumps(self, default=mongoencode)

class User(Document, UserMixin, Base):
    name = StringField()
    screen_name = StringField()
    access_token_key = StringField()
    access_token_secret = StringField()

class Article(Document, Base):
    title = StringField()
    url = StringField()
    text = StringField()
    author = StringField()
    summary = StringField()

    media = ListField()
    date = StringField()

    category = StringField()
    language = StringField(default="en")

    @classmethod
    def build_from_json(cls, json, category):
        article = cls()
        article.title = json.get('title','')
        article.url = json.get('url','')
        article.text = json.get('text','')
        article.author = json.get('author','')
        article.summary = json.get('summary','')

        article.media = json.get('media','')
        article.date = json.get('date','')

        article.category = category

        try:
            article.save()
        except:
            return None

        return article