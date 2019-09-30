class Config(object):
    PERMANENT_SESSION_LIFETIME = 12 * 3600  # in seconds.
    SECRET_KEY = 'calico'

    # Flask-Babel config.
    BABEL_DEFAULT_LOCALE = 'id_ID'

    # Flask-WTF config.
    WTF_CSRF_TIME_LIMIT = 3600  # in seconds.

    # Template texts.
    APP_NAME = 'FA3 Starter Kit'
    COPYRIGHT_TEXT = '&copy; 2019 Poerwiyanto.'


class Dev(Config):
    # Flask config.
    DEBUG = True
    ENV = 'development'
    HOST = '0.0.0.0'
    PORT = 5001

    # Flask-SQLAlchemy config.
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/mylab'
    TABLE_PREFIX = 'app_'


class Prod(Config):
    # Flask config.
    DEBUG = False
    ENV = 'production'
    HOST = '0.0.0.0'
    PORT = 5001

    # Flask-SQLAlchemy config.
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/mylab'
    TABLE_PREFIX = ''
