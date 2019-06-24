from sanic import Blueprint

from app.api.v7.users import GetAllUsersView, GetUserByIdView, UpdateUserByIdView, AddUserView, DeleteUserByIdView


api_v7_blueprint = Blueprint('api_v7', url_prefix='/v7')

api_v7_blueprint.add_route(GetAllUsersView.as_view(), uri='/users', methods=['GET'])
api_v7_blueprint.add_route(GetUserByIdView.as_view(), uri='/users/<user_id:int>', methods=['GET'])
api_v7_blueprint.add_route(UpdateUserByIdView.as_view(), uri='/users/<user_id>', methods=['PUT'])
api_v7_blueprint.add_route(AddUserView.as_view(), uri='/users', methods=['POST'])
api_v7_blueprint.add_route(DeleteUserByIdView.as_view(), uri='/users/<user_id>', methods=['DELETE'])
