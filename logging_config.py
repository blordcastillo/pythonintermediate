import logging.config
from string import punctuation
from string import whitespace
import json
import os


class KeywordFilter(logging.Filter):
    def __init__(self, param=None):
        super(KeywordFilter, self).__init__()
        self.param = param

    def filter(self, record):
        if self.param is None:
            allow = True
        else:
            allow = record.msg.startswith(self.param)
        if allow:
            record.msg = record.msg[len(self.param):].lstrip(punctuation + whitespace)
        return allow


def setup_logging(
        default_path='logging.json',
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
