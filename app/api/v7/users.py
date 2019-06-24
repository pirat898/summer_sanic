from sanic.exceptions import NotFound

from app.api.models.user import User
from app import db_api
from app.api.v7.base_http_method_view import BaseHTTPMethodView


class GetAllUsersView(BaseHTTPMethodView):
    result_model = User

    async def get(self, request):
        users = await db_api.get_all_users()
        return users


class GetUserByIdView(BaseHTTPMethodView):
    result_model = User

    async def get(self, request, user_id):
        user = await db_api.get_user_by_id(user_id)
        if user:
            return user
        raise NotFound(f'User with id {user_id} not found')


class UpdateUserByIdView(BaseHTTPMethodView):
    body_model = User
    result_model = User

    async def put(self, request, user_id):
        user = await db_api.update_user_by_id(user_id, self.body_params)
        if user:
            return user
        raise NotFound(f'User with id {user_id} not found')


class AddUserView(BaseHTTPMethodView):
    body_model = User
    result_model = User

    async def post(self, request):
        user = await db_api.add_user(self.body_params)
        self.status_code = 201
        return user


class DeleteUserByIdView(BaseHTTPMethodView):
    async def delete(self, request, user_id):
        await db_api.delete_user_by_id(user_id)
        self.status_code = 204
        return None
