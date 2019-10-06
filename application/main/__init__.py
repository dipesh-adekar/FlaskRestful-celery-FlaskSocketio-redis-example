from flask import Blueprint

application_model = Blueprint("application", __name__)

from . import routes, events