from sanic.response import json
from sanic.views import HTTPMethodView
from sanic_openapi import doc

from app.test_data.users import users
# from app.api.v3.models.user import User


class User:
    user_id = doc.Integer(description='descr user_id')
    age = doc.Integer(description='descr age')
    name = doc.String(description='descr name')
    phone = doc.String(description='descr phone')


# @doc.summary('Add user')
# @doc.consumes(User, content_type="application/json", location="body")
# @doc.produces(User)
class AddUserView(HTTPMethodView):

    async def post(self, request):
        # user = User(request.json)
        # user.validate()
        # user_id = max(users.keys()) + 1
        # users[user_id] = user.to_primitive()
        # return json(user.to_primitive(), status=201)
        return json({'user_id': 33, 'name': 'ffff', 'age': 123, 'phone': '99875467'})
