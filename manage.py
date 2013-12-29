from flask.ext.script import Manager, Shell

from sababa import app

from mongoengine import *

from sababa import models
from sababa.models import *

manager = Manager(app)

def _make_context():
    return {'app': app, 'models': models}

@manager.command
def delete_and_bootstrap():
    pass

if __name__ == "__main__":
    manager.add_command('shell', Shell(make_context=_make_context))
    manager.run()