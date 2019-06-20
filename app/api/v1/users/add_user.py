from sanic.response import json
from sanic.views import HTTPMethodView

from app.test_data.users import users


class AddUserView(HTTPMethodView):

    async def post(self, request):
        user = request.json
        user_id = max(users.keys()) + 1
        users[user_id] = user
        return json(user, status=201)
