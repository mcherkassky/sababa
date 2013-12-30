__author__ = 'mcherkassky'

import goslate

gs = goslate.Goslate()

languages = {'Hebrew': 'iw',
             'English': 'en'}

def translate(text, language):
    return gs.translate(text, languages[language])

