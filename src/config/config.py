import os
import json
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load PostgreSQL credentials from .env file
POSTGRES_USERNAME = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = quote_plus(os.getenv('POSTGRES_PASSWORD'))

# Load configuration from config.json
with open('./config/config.json') as config_file:
    config = json.load(config_file)

# Export configuration
DB_CONFIG = {
    'username': POSTGRES_USERNAME,
    'password': POSTGRES_PASSWORD,
    'database': config['database'],
    'host': config['host'],
    'port': config['port'],
}

PIPELINE_CONFIG = config['data']

