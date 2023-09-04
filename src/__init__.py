__all__ = ['client', 'service']

from src.core.client import init_client
from src.core.service import init_service


# ----------------------------------------------------------------
# initialize client and service
client = init_client()
service = init_service()
