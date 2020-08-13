import os
from os import getenv
from asyncio import set_event_loop, new_event_loop

APP_DIR = os.path.dirname(__file__)
MIGRATION_DIR = os.path.join(APP_DIR, 'migrations')


class Config:
    DEBUG = getenv('DEBUG', bool)
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    POSTGRES_DB = getenv('POSTGRES_DB', 'db')
    POSTGRES_USER = getenv('POSTGRES_USER', 'user')
    POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD', 'password')
    POSTGRES_HOST = getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = getenv('POSTGRES_PORT', 5400)
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:' \
                              f'{POSTGRES_PORT}/{POSTGRES_DB}'

    # asincio loop
    LOOP = new_event_loop()
    set_event_loop(LOOP)
