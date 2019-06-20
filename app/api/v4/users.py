from sanic.response import json
from sanic.exceptions import NotFound, InvalidUsage
from schematics.exceptions import BaseError
from sanic_openapi import doc

from app.api.v4.models.user import UserById, User
from app import db_api


class UserInputModel:
    age = doc.Integer(description='User age')
    name = doc.String(description='User name')
    phone = doc.String(description='User phone')


class UserOutputModel:
    user_id = doc.Integer(description='User identifier')
    age = doc.Integer(description='User age')
    name = doc.String(description='User name')
    phone = doc.String(description='User phone')


@doc.summary('Get all users')
@doc.produces(UserOutputModel)
async def get_all_users_method(request):
    users = await db_api.get_all_users()
    return json(users, status=200)


@doc.summary('Get user by id')
@doc.produces(UserOutputModel)
async def get_user_by_id_method(request, user_id):
    user = await db_api.get_user_by_id(UserById({'user_id': user_id}).user_id)
    if user:
        return json(user, status=200)
    raise NotFound(f'User with id {user_id} not found')


@doc.summary('Update user')
@doc.consumes(UserInputModel, content_type="application/json", location="body")
@doc.produces(UserOutputModel)
async def update_user_by_id_method(request, user_id):
    user_id = UserById({'user_id': user_id}).user_id
    user = User(request.json, strict=True)
    try:
        user.validate()
    except BaseError as ex:
        raise InvalidUsage(f'Error in data: {ex.to_primitive()}')

    user = db_api.update_user_by_id(user_id, user.to_native())
    return json(user, status=200)


@doc.summary('Add new user')
@doc.consumes(UserInputModel, content_type="application/json", location="body")
@doc.produces(UserOutputModel)
async def add_user_method(request):
    user = User(request.json, strict=True)
    try:
        user.validate()
    except BaseError as ex:
        raise InvalidUsage(f'Error in data: {ex.to_primitive()}')

    user = await db_api.add_user(user.to_native())
    return json(user, status=201)


@doc.summary('Delete user')
async def delete_user_by_id_method(request, user_id):
    await db_api.delete_user_by_id(UserById({'user_id': user_id}).user_id)
    return json({}, status=204)
