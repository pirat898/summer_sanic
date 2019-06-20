from sanic import Blueprint

from app.api.v1.blueprint import api_v1_blueprint
from app.api.v2.blueprint import api_v2_blueprint
from app.api.v3.blueprint import api_v3_blueprint

api_blueprint_group = Blueprint.group([
    api_v1_blueprint,
    api_v2_blueprint,
    api_v3_blueprint
],
    url_prefix='/api')
