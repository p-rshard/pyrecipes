"""Module for custom error pages"""

from flask import Blueprint

blueprint = Blueprint("errors", __name__, template_folder="templates")
