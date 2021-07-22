import os
from configparser import ConfigParser


class Config:
    try:
        INI_PATH = os.path.join(os.path.dirname(__file__), 'config.local.ini')
    except OSError:
        INI_PATH = os.path.join(os.path.dirname(__file__), 'config.ini')

    __parser = ConfigParser()
    __parser.read(INI_PATH)

    BASE_URL = __parser.get('api', 'base_url')
    ADMIN_USER = __parser.get('api', 'admin_user')
    ADMIN_PASS = __parser.get('api', 'admin_pass')
    ADMIN_PASS = ADMIN_PASS if ADMIN_PASS else os.environ['ADMIN_PASS']

    LOG_LEVEL = __parser.get('common', 'log_level')
