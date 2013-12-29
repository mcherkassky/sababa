from flask import render_template
from flask.ext.login import login_required

from sababa import app

@app.route('/')
def index():
    return render_template('index/index.html')
