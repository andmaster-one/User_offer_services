import os

class Settings:
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", "5432")
    DB_USER = os.environ.get("DB_USER", 'postgres')
    DB_PASSWORD = os.environ.get("DB_PASSWORD", 'postgres')
    DB_DATABASE = os.environ.get("DB_DATABASE", 'postgres')

    DEBUG = bool(int(os.environ.get("DEBUG", 1)))
    AUTO_RELOAD = bool(int(os.environ.get("AUTO_RELOAD", 0)))

    HOST = os.environ.get("HOST", '0.0.0.0')
    PORT = os.environ.get("PORT", 9000)
   
    SECRET_KEY = os.environ.get("SECRET_KEY", 'secret')

OFFER_SERVICE_HOST = os.environ.get("OFFER_SERVICE_HOST", 'localhost')
OFFER_SERVICE_PORT = os.environ.get("OFFER_SERVICE_PORT", 9001)
OFFER_API_URLS = {
    'offer' : 'http://' + OFFER_SERVICE_HOST + ':' + str(OFFER_SERVICE_PORT) + '/offer'
}

ERROR_MESSAGES = {
    'ERROR_JSON': 'Error JSON parsing'
    }

