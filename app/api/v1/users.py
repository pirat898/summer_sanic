from sanic.response import json

from app import db_api


async def get_all_users_method(request):
    users = await db_api.get_all_users()
    return json(users, status=200)


async def get_user_by_id_method(request, user_id):
    user = await db_api.get_user_by_id(user_id)
    return json(user, status=200)


async def update_user_by_id_method(request, user_id):
    user = db_api.update_user_by_id(user_id, request.json)
    return json(user, status=200)


async def add_user_method(request):
    user = await db_api.add_user(request.json)
    return json(user, status=201)


async def delete_user_by_id_method(request, user_id):
    await db_api.delete_user_by_id(user_id)
    return json({}, status=204)
