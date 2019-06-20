from sanic.response import json
from sanic.views import HTTPMethodView

from app.test_data.users import users
from app.api.v3.models.user import UserById, User


class UserByIdView(HTTPMethodView):

    async def patch(self, request, user_id):
        user_id = UserById({'user_id': user_id}).user_id
        user = users.get(user_id)
        user = User({**user, **request.json}, strict=True)
        user.validate()
        users[user_id] = user.to_primitive()
        return json(user.to_primitive(), status=200)

    async def delete(self, request, user_id):
        user_id = UserById({'user_id': user_id}).user_id
        users.pop(user_id)
        return json({}, status=200)
