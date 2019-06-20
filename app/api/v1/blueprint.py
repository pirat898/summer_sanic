from sanic import Blueprint

from app.api.v1.users.get_user_by_id import UserByIdView
from app.api.v1.users.add_user import AddUserView


api_v1_blueprint = Blueprint('api_v1', url_prefix='/v1')

api_v1_blueprint.add_route(UserByIdView.as_view(), uri='/users/<user_id>')
api_v1_blueprint.add_route(AddUserView.as_view(), uri='/users')
