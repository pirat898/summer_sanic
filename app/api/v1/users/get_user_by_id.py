from sanic.response import json
from sanic.views import HTTPMethodView

from app.test_data.users import users


class UserByIdView(HTTPMethodView):

    async def get(self, request, user_id):
        user_id = int(user_id)
        user = users.get(user_id)
        return json(user, status=200)

    async def patch(self, request, user_id):
        user_id = int(user_id)
        user = users.get(user_id)
        user = {**user, **request.json}
        users[user_id] = user
        return json(user, status=200)

    async def delete(self, request, user_id):
        user_id = int(user_id)
        users.pop(user_id)
        return json({}, status=200)
