import os


class Config(object):
    HOST = "0.0.0.0"
    PORT = 8000
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'lomojo supper cai'
    postgres_host = os.getenv('POSTGRESHOST', 'localhost')
    postgres_passwd = os.getenv('POSTGRESPASSWD', '')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:%s@%s/lomojo' % (postgres_passwd, postgres_host)


class ProdConfig(Config):
    pass


class DevConfig(Config):
    ENV = "development"
    DEBUG = True

