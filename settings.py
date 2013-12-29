MONGO_HOST = "paulo.mongohq.com"
MONGO_DATABASE_NAME = "sababa"
MONGO_PORT = 10093

MONGO_USERNAME = "israel"
MONGO_PASSWORD = "tech"

HOST = 'http://127.0.0.1:5000'

# access_key='1552105075-fDyEqGl2qTOgFzdfJZAOAkZwlXdq7AXRxs2OZm4'
# access_secret='hbEZp3o075kvf7DS2v3RGhE9CGAzjzIVnqLI16w5kDGvK'

try:
    from settings_local import *
except:
    pass
