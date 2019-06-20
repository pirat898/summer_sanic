from sanic import Blueprint

from app.api.v3.users.get_user_by_id import GetUserByIdView
from app.api.v3.users.user_by_id import UserByIdView
from app.api.v3.users.add_user import AddUserView


api_v3_blueprint = Blueprint('api_v3', url_prefix='/v3', strict_slashes=True)

api_v3_blueprint.add_route(UserByIdView.as_view(), uri='/users/<user_id>')
api_v3_blueprint.add_route(GetUserByIdView.as_view(), uri='/users/<user_id>')
api_v3_blueprint.add_route(AddUserView.as_view(), uri='/users')
