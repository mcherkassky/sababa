from flask import url_for, request, redirect, render_template, session, g
from flask.ext.login import current_user, login_user
from settings import *
from sababa import app
from sababa.models import *
import requests
from sababa.rank.translate import translate

print 'starting context index'

#similar wwords shit
# import nltk
# idx = nltk.text.ContextIndex([word.lower( ) for word in nltk.corpus.brown.words( ) + nltk.corpus.reuters.words()])

print 'finished context index'



@app.route('/user/<user_id>/translate/<text>', methods=['GET'])
def trans(text, user_id):
    user = User.objects.get(user_id=user_id)
    language = user.native
    return translate(text, language)

@app.route('/user/<user_id>/<feedback>', methods=['GET'])
def score(user_id, feedback):
    user = User.objects().get(user_id=user_id)
    if feedback == "correct":
        user.level += .1
    elif feedback == "incorrect":
        user.level -= .1
    else:
        pass

    user.level = max(min(user.level, 1), 0)
    user.save()
    return user.to_json()


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

    # question = {"header": "Test your understanding",
    #             "text": "What is this thing?",
    #             "choices": ["a", "b", "c"],
    #             "answerText": "b",
    #             "answerNum": 2}
    question = article.get_question()
    words = article.get_words()

    response = '{' + '"article":{},"question":{}, "words":{}'.format(article.to_json(), json.dumps(question), json.dumps(words)) + '}'

    return response
