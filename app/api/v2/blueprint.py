from sanic import Blueprint

from app.api.v2.users.get_user_by_id import UserByIdView
from app.api.v2.users.add_user import AddUserView


api_v2_blueprint = Blueprint('api_v2',
                             url_prefix='/v2')

api_v2_blueprint.add_route(UserByIdView.as_view(),
                           uri='/users/<user_id>')
api_v2_blueprint.add_route(AddUserView.as_view(),
                           uri='/users')
