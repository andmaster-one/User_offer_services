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
    PORT = os.environ.get("PORT", 9001)
   
    SECRET_KEY = os.environ.get("SECRET_KEY", 'secret')

USER_SERVICE_HOST = os.environ.get("USER_SERVICE_HOST", 'localhost')
USER_SERVICE_PORT = os.environ.get("USER_SERVICE_PORT", 9000)

USER_API_URLS = {
    'user' : 'http://' + USER_SERVICE_HOST + ':' + str(USER_SERVICE_PORT) + '/user'
}

ERROR_MESSAGES = {
    'ERROR_JSON': 'Error JSON parsing'
    }




    
