from settings import DIFFBOT_TOKEN
from diffbot import DiffBot

api = DiffBot(DIFFBOT_TOKEN)

import pdb; pdb.set_trace()
api.article('http://google.com', summary=True)
