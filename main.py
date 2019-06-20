from sanic import Sanic
# from sanic_openapi import swagger_blueprint

from app.api.blueprint_group import api_blueprint_group


async def before_server_start(app, loop):
    print(f"Before server start")


async def before_server_stop(app, loop):
    print(f"Before server stop")


if __name__ == "__main__":
    web_app = Sanic()

    web_app.listener('before_server_start')(before_server_start)
    web_app.listener('before_server_stop')(before_server_stop)

    web_app.blueprint(api_blueprint_group)
    # web_app.blueprint(swagger_blueprint)

    web_app.config.API_VERSION = '1.0.0'
    web_app.config.API_TITLE = 'Summer Sanic'
    web_app.config.API_DESCRIPTION = 'Summer Sanic'
    web_app.config.API_PRODUCES_CONTENT_TYPES = ['application/json']

    web_app.run(host="0.0.0.0", port=8080, debug=True, auto_reload=False)
