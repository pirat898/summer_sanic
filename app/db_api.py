import aiopg
from psycopg2.extras import DictCursor

DB_URL = 'postgresql://user:pass@127.0.0.1:5434/test'


async def get_all_users():
    query = 'select user_id, name, age, phone from users limit 100 ;'
    async with aiopg.connect(DB_URL) as conn:
        async with conn.cursor(cursor_factory=DictCursor) as cur:
            await cur.execute(query)
            data = await cur.fetchall()
            return [dict(u) for u in data]


async def get_user_by_id(user_id):
    query = 'select user_id, name, age, phone from users where user_id = %(user_id)s ;'
    async with aiopg.connect(DB_URL) as conn:
        async with conn.cursor(cursor_factory=DictCursor) as cur:
            await cur.execute(query, {'user_id': user_id})
            data = await cur.fetchone()
            if data:
                return dict(data)


async def update_user_by_id(user_id, user_data):
    query = '''update users set name = %(name)s, age = %(age)s, phone = %(phone)s 
               where user_id = %(user_id)s 
               returning user_id, name, age, phone
               ;'''
    params = {'user_id': user_id, 'name': user_data.get('name'), 'age': user_data.get('age'), 'phone': user_data.get('phone')}
    async with aiopg.connect(DB_URL) as conn:
        async with conn.cursor(cursor_factory=DictCursor) as cur:
            await cur.execute(query, params)
            data = await cur.fetchone()
            if data:
                return dict(data)


async def add_user(user_data):
    query = '''insert into users (name, age, phone) 
               values (%(name)s, %(age)s, %(phone)s )
               returning user_id, name, age, phone
               ;'''
    params = {'name': user_data.get('name'), 'age': user_data.get('age'), 'phone': user_data.get('phone')}
    async with aiopg.connect(DB_URL) as conn:
        async with conn.cursor(cursor_factory=DictCursor) as cur:
            await cur.execute(query, params)
            data = await cur.fetchone()
            return dict(data)


async def delete_user_by_id(user_id):
    query = 'delete from users where user_id = %(user_id)s ;'
    async with aiopg.connect(DB_URL) as conn:
        async with conn.cursor(cursor_factory=DictCursor) as cur:
            await cur.execute(query, {'user_id': user_id})
