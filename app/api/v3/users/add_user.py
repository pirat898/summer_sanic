from sanic.response import json
from sanic.views import HTTPMethodView

from app.test_data.users import users
from app.api.v3.models.user import User


class AddUserView(HTTPMethodView):

    async def post(self, request):
        user = User(request.json)
        user.validate()
        user_id = max(users.keys()) + 1
        users[user_id] = user.to_primitive()
        return json(user.to_primitive(), status=201)
