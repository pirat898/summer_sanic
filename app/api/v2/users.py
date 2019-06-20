from sanic.response import json

from app.api.v2.models.user import UserById, User
from app import db_api


async def get_all_users_method(request):
    users = await db_api.get_all_users()
    return json(users, status=200)


async def get_user_by_id_method(request, user_id):
    user = await db_api.get_user_by_id(UserById({'user_id': user_id}).user_id)
    if user:
        return json(user, status=200)
    return json({}, status=404)


async def update_user_by_id_method(request, user_id):
    user_id = UserById({'user_id': user_id}).user_id
    user = User(request.json, strict=True)
    user.validate()
    user = db_api.update_user_by_id(user_id, user.to_native())
    return json(user, status=200)


async def add_user_method(request):
    user = User(request.json, strict=True)
    user.validate()
    user = await db_api.add_user(user.to_native())
    return json(user, status=201)


async def delete_user_by_id_method(request, user_id):
    await db_api.delete_user_by_id(UserById({'user_id': user_id}).user_id)
    return json({}, status=204)
