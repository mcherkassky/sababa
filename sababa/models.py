from mongoengine import *
from flask_login import UserMixin
import json
import re

from bs4 import *
from random import shuffle, sample
from bson import json_util, ObjectId, DBRef
from mongoengine.dereference import DeReference
from mongoengine.queryset import Q
from random import choice
import requests

from sababa.rank import distribution
from sababa.rank.rank import rank_article

import rank

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
    user_id = StringField()

    level = FloatField(default=.5)

    native = StringField(default="Hebrew")
    learning = StringField(default="English")

    def get_article(self, category):
        if category == 'Random':
            category = choice(['Entertainment',
                               'Technology',
                               'Art',
                               'Sports',
                               'Business',
                               'Politics',
                               'Health',
                               'Science'])
        score = self.level

        top_score = score + .05
        bottom_score = score - .05

        articles = Article.objects(Q(rank__gte=bottom_score) & Q(rank__lte=top_score) & Q(category=category))
        selected = choice(articles)
        return selected

def similar_words(word):
    r = requests.get('http://api.wordnik.com:80/v4/word.json/{}/relatedWords?useCanonical=false&relationshipTypes=same-context&limitPerRelationshipType=10&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'.format(word))

    return r.json()[0]['words']

class Article(Document, Base):
    title = StringField()
    url = StringField()
    text = StringField()
    author = StringField()
    summary = StringField()

    media = ListField()
    date = StringField()

    score = FloatField(default=0)
    rank = FloatField()

    category = StringField()
    language = StringField(default="en")

    def get_words(self):
        score_out = rank_article(self.text, distribution)[1]

        words = score_out.keys()
        return words

    def get_question(self):
        score_out = rank_article(self.text, distribution)[1]

        answer = choice(score_out.keys())
        question = score_out[answer].replace('\n', '')

        pattern = re.compile(answer, re.IGNORECASE)
        question = pattern.sub('_______', question)

        try:
            choices = sample([word for word in self.get_words() if word != answer], 2) + [answer]
        except:
            choices = ['apprehensive', 'dictator'] + [answer]

        shuffle(choices)

        answer_index = choices.index(answer)

        out = {"header": "Fill in the blank",
                "text": question,
                "choices": choices,
                "answerText": answer,
                "answerNum": answer_index}

        return out

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