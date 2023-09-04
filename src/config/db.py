from pydantic_settings import BaseSettings


# ----------------------------------------------------------------
class DBSettings(BaseSettings):
    """
    Class defines connection params for ClickHouse database
    """
    user: str
    password: str
    host: str
    port: str
    name: str
