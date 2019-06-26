from sanic.exceptions import NotFound
from sanic_transmute import describe

from app.api.models.user import UserById, InputUser, OutputUser
from app import db_api


@describe(paths="/users", methods="GET", tags=['users'])
async def get_all_users_method(request) -> [OutputUser]:
    """Get all users"""
    users = await db_api.get_all_users()
    return [OutputUser(user, strict=False) for user in users]


@describe(paths="/users/{user_id}", methods="GET", parameter_descriptions={'user_id': 'id of user to get'},
          tags=['users'], )
async def get_user_by_id_method(request, user_id: int) -> OutputUser:
    """Get user by id"""
    user = await db_api.get_user_by_id(UserById({'user_id': user_id}).user_id)
    if user:
        return OutputUser(user, strict=False)
    raise NotFound(f'User with id {user_id} not found')


@describe(paths="/users/{user_id}", methods="PUT", parameter_descriptions={'user_id': 'id of user to update'},
          tags=['users'])
async def update_user_by_id_method(request, user_id: int, user: InputUser) -> OutputUser:
    """Update user info by id"""
    user_id = UserById({'user_id': user_id}).user_id
    user = await db_api.update_user_by_id(user_id, user.to_native())
    return OutputUser(user, strict=False)


@describe(paths='/users', methods="POST", success_code=201, tags=['users'])
async def add_user_method(request, user: InputUser) -> OutputUser:
    """Add new user"""
    user = await db_api.add_user(user.to_native())
    return OutputUser(user, strict=False)


@describe(paths='/users/{user_id}', methods="DELETE", parameter_descriptions={'user_id': 'id of user to delete'},
          success_code=204, tags=['users'])
async def delete_user_by_id_method(request, user_id: int) -> None:
    """Delete user by id"""
    await db_api.delete_user_by_id(user_id)
