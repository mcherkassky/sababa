from flask.ext.script import Manager, Shell

from sababa import app

from mongoengine import *
import re
from sababa import models
from sababa.models import *

from sababa.rank import distribution
from sababa.rank.rank import rank_article


manager = Manager(app)

def _make_context():
    return {'app': app, 'models': models}

@manager.command
def format_text():
    articles = models.Article.objects()

    for article in articles:
        article.text = re.sub('(\n)+', '\n', article.text)
        article.text = re.sub('\n', '\n\n', article.text)

        article.save()

@manager.command
def score_articles():
    articles = models.Article.objects()

    for article in articles:
        if article.score:
            continue
        else:
            article.score = rank_article(article.text, distribution)[0][1] #score article
            article.save()


if __name__ == "__main__":
    manager.add_command('shell', Shell(make_context=_make_context))
    manager.run()