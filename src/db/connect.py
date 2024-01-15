import sys
from sqlalchemy import create_engine
from config.config import DB_CONFIG
from utils.logger import setup_logger

# Get logger
log = setup_logger()


def connect_to_db() -> object:
    """
    Connects to the database using the provided configuration.

    Returns:
        object: The database engine object.
    """

    try:
        engine = create_engine(
            f"postgresql://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}")
        log.info('Connected to the database.')
    except Exception as e:
        log.error(f'Could not connect to the database. Error: {e}')
        sys.exit(1)
    
    return engine