from settings import DIFFBOT_TOKEN, BING_KEY
from diffbot import DiffBot
import requests
from bs4 import BeautifulSoup
import urllib2

import lxml
from time import sleep

from sababa.models import Article

#feedzilla categories
categories = {'Sports': 27,
              'Business': 22,
              'Technology': 30,
              'Politics': 3,
              'Health': 11,
              'Entertainment': 6,
              'Science': 8}

api = DiffBot(DIFFBOT_TOKEN)
# api.article('http://google.com', summary=True)

def open_landing(url, counter=1):
    try:
        landing = BeautifulSoup(urllib2.urlopen(url).read(), 'lxml')
        return landing
    except:
        print(counter)
        if counter == 3:
            return None
        counter += 1
        open_landing(url, counter)

def fetch_news(code):
    response = requests.get('http://api.feedzilla.com/v1/categories/{}/articles.json?count=100'.format(code))
    return [article['url'] for article in response.json()['articles']]

for key in categories.keys():
    articles = fetch_news(categories[key])

    for (index, article) in enumerate(articles):
        landing = open_landing(article)
        if landing is None:
            continue
        redirect = landing.find('iframe').get('src')

        print 'analyzing {}: number {}'.format(key, index)
        summary = api.article(redirect, summary=True)
        sleep(1)
        Article.build_from_json(summary, key)