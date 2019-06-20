from sanic import Blueprint

from app.api.v4.users import get_all_users_method, update_user_by_id_method, add_user_method, get_user_by_id_method, \
    delete_user_by_id_method


api_v4_blueprint = Blueprint('api_v4', url_prefix='/v4', strict_slashes=True)

api_v4_blueprint.add_route(get_all_users_method, uri='/users', methods=['GET'])
api_v4_blueprint.add_route(get_user_by_id_method, uri='/users/<user_id>', methods=['GET'])
api_v4_blueprint.add_route(update_user_by_id_method, uri='/users/<user_id>', methods=['PUT'])
api_v4_blueprint.add_route(add_user_method, uri='/users', methods=['POST'])
api_v4_blueprint.add_route(delete_user_by_id_method, uri='/users/<user_id>', methods=['DELETE'])
