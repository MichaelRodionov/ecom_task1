from src.service import Service


# ----------------------------------------------------------------
def init_service() -> Service:
    """
    Method to initialize service obj

    Params:
        - data: list of records from db
    """
    return Service()
