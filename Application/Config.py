class AppConfig(object):
    DEBUG = True
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = r'mysql://user:password@address:port/database?charset=utf8'
    SCHEDULER_API_ENABLED = True
