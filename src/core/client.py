from src.config import settings


# ----------------------------------------------------------------
def init_client():
    """
    Method to initialize clickhouse client
    """
    return settings.client
