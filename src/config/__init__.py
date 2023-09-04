__all__ = ['settings']

import os

import clickhouse_connect
from dotenv import load_dotenv
from pydantic import BaseConfig
from .db import DBSettings

# ----------------------------------------------------------------
# load env variables
load_dotenv()


# ----------------------------------------------------------------
class Settings(BaseConfig):
    title: str = 'API task1'
    db: DBSettings = DBSettings(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        name=os.getenv('DB_NAME'),
    )
    client = clickhouse_connect.get_client(
        username=db.user,
        password=db.password,
        host=db.host,
        port=db.port,
        database=db.name
    )


# ----------------------------------------------------------------
# init app settings obj
settings: Settings = Settings()
