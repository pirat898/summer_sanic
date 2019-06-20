from sanic.response import json

from app.test_data.users import users
from app.api.v3.models.user import UserById, User
from app.api.v3.base_http_method_view import BaseHTTPMethodView


class GetUserByIdView(BaseHTTPMethodView):
    body_model = None
    url_model = UserById
    result_model = User

    async def get(self, request, user_id):
        model = UserById({'user_id': user_id})
        user = users.get(model.user_id)
        return json(user, status=200)
