from sanic import Blueprint

from app.api.v6.users import GetAllUsersView, GetUserByIdView, UpdateUserByIdView, AddUserView, DeleteUserByIdView


api_v6_blueprint = Blueprint('api_v6', url_prefix='/v6')

api_v6_blueprint.add_route(GetAllUsersView.as_view(), uri='/users', methods=['GET'])
api_v6_blueprint.add_route(GetUserByIdView.as_view(), uri='/users/<user_id>', methods=['GET'])
api_v6_blueprint.add_route(UpdateUserByIdView.as_view(), uri='/users/<user_id>', methods=['PUT'])
api_v6_blueprint.add_route(AddUserView.as_view(), uri='/users', methods=['POST'])
api_v6_blueprint.add_route(DeleteUserByIdView.as_view(), uri='/users/<user_id>', methods=['DELETE'])
