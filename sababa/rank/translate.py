__author__ = 'mcherkassky'

import goslate

gs = goslate.Goslate()

languages = {'Hebrew': 'iw',
             'English': 'en',
             'French': 'fr',
             'Spanish': 'sp',
             'Mandarin': 'zh',
             'Japanese': 'ja',
             'Italian': 'it',
             'German': 'de'}

def translate(text, language):
    return gs.translate(text, languages[language])

