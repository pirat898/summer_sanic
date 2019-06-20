from sanic.response import json
from sanic import Sanic


async def hello(request):
    return json({'hello': 'world'})


if __name__ == "__main__":
    web_app = Sanic()
    web_app.add_route(hello, '/hello')
    web_app.run(host="0.0.0.0", port=8080)
