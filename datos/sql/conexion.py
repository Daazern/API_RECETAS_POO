from decouple import config
from peewee import MySQLDatabase


def conectar():
    return MySQLDatabase(
        config('MySQLDatabase'),
        charset='utf8mb4',
        host=config('host'),
        port=config('port', cast=int),
        user=config('user'),
        password=config('password'),
    )
