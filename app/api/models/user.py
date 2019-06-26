from schematics import Model, types


class User(Model):
    user_id = types.IntType()
    age = types.IntType(min_value=0, max_value=99)
    name = types.StringType(required=True)
    phone = types.StringType()


class UserById(Model):
    user_id = types.IntType(required=True)


class InputUser(Model):
    age = types.IntType(min_value=0, max_value=99)
    name = types.StringType(required=True)
    phone = types.StringType()


class OutputUser(InputUser):
    user_id = types.IntType()


class SanicError(Model):
    success: types.BooleanType()
    result: types.StringType()
    code: types.IntType()
