from flask.ext.script import Manager, Shell

from sababa import app

from mongoengine import *

from sababa import models
from sababa.models import *

manager = Manager(app)

def _make_context():
    return {'app': app, 'models': models}

@manager.command
def format_text():
    articles = models.Article.objects()
    
    for article in articles:
        import pdb; pdb.set_trace()

        article.text = re.sub('(\n)+', '\n', article.text)
        article.text = re.sub('\n', '\n\n', article.text)

        article.save()


if __name__ == "__main__":
    manager.add_command('shell', Shell(make_context=_make_context))
    manager.run()