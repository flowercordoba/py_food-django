import os
import logging
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()
logger = logging.getLogger(__name__)

def get_postgres_config():
    tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

    logger.info(
        f"Connecting to PostgreSQL at {tmpPostgres.hostname}:{tmpPostgres.port or 5432}, "
        f"DB: {tmpPostgres.path.lstrip('/')}"
    )

    return {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': tmpPostgres.path.lstrip('/'),
            'USER': tmpPostgres.username,
            'PASSWORD': tmpPostgres.password,
            'HOST': tmpPostgres.hostname,
            'PORT': tmpPostgres.port or 5432,
        }
    }
