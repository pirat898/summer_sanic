from schematics import Model, types


class User(Model):
    user_id = types.IntType()
    age = types.IntType(min_value=0, max_value=99)
    name = types.StringType(required=True)
    phone = types.StringType(regex=r'^\d{10}$')
