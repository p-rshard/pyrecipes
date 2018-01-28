"""Application configuration"""

import os


#pylint: disable=too-few-public-methods
class Config(object):
    """Configuration base class"""

    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevConfig(Config):
    """Class for development configuration"""
    pass


class ProdConfig(Config):
    """Class for production configuration"""
    pass
