from flask import Flask
# from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine

# import db

import settings

app = Flask(__name__)

app.debug = True
app.secret_key = 'zefr'

app.config.from_object(settings)
db = MongoEngine(app)

# login_manager = LoginManager()
# login_manager.init_app(app)

from views.index import *
from views.api import *