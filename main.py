"""Start applicatoion"""

from flask.helpers import get_debug_flag
from pyrecipes.app import create_app
from pyrecipes.configuration import DevConfig, ProdConfig

debug = get_debug_flag()
config = DevConfig if debug else ProdConfig

app = create_app(config)
