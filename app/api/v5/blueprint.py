from sanic import Blueprint
from sanic_transmute import add_route

from app.api.v5.users import get_all_users_method, update_user_by_id_method, add_user_method, get_user_by_id_method, \
    delete_user_by_id_method


api_v5_blueprint = Blueprint('api_v5', url_prefix='/v5')

add_route(api_v5_blueprint, get_all_users_method)
add_route(api_v5_blueprint, get_user_by_id_method)
add_route(api_v5_blueprint, update_user_by_id_method)
add_route(api_v5_blueprint, add_user_method)
add_route(api_v5_blueprint, delete_user_by_id_method)
