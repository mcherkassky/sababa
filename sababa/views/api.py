from flask import url_for, request, redirect, render_template, session, g
from flask.ext.login import current_user, login_user
from settings import *
from sababa import app
from sababa.models import *

@app.route('/test', methods=["POST"])
def test():
    import pdb; pdb.set_trace()

@app.route('/user/<user_id>', methods=['POST', 'GET'])
def user(user_id):
    if request.method == 'POST':
        data = request.json

        try:
            user = User.objects.get(user_id=user_id)
        except:
            user = User(user_id=user_id)
        for key, value in data.items():
            user[key] = value

        user.save()
        return user.to_json()

    elif request.method == 'GET':
        user = User.objects().get(user_id=user_id)
        return user.to_json()
    else:
        return 404


@app.route('/user/<user_id>/article/<article_type>', methods=['GET'])
def article(user_id, article_type):
    user = User.objects().get(user_id=user_id)

    article = user.get_article(article_type)

    return article.to_json()
