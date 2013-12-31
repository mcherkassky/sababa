MONGO_HOST = "alex.mongohq.com"
MONGO_DATABASE_NAME = "sababa_copy2"
MONGO_PORT = 10010

MONGO_USERNAME = "israel"
MONGO_PASSWORD = "tech"

# HOST = 'http://127.0.0.1:5000'

MONGODB_SETTINGS = {
    "DB": MONGO_DATABASE_NAME,
    "USERNAME": MONGO_USERNAME,
    "PASSWORD": MONGO_PASSWORD,
    "HOST": MONGO_HOST,
    "PORT": MONGO_PORT
}

DIFFBOT_TOKEN = 'd7e4938b7beea0bfe73cae0e3030bb8f'
BING_KEY = 'Uumxw9jqa+ILOAQDXBisO2zPsgs6zz+ZzOWss8H6GKg'
# access_key='1552105075-fDyEqGl2qTOgFzdfJZAOAkZwlXdq7AXRxs2OZm4'
# access_secret='hbEZp3o075kvf7DS2v3RGhE9CGAzjzIVnqLI16w5kDGvK'

try:
    from settings_local import *
except:
    pass
